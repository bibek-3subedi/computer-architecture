def add(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    
    result = []
    carry = 0
    
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result.append('1' if r % 2 == 1 else '0')
        carry = 1 if r >= 2 else 0
        
    if carry:
        result.append('1')
        
    return ''.join(reversed(result))


def complement(val):
    # Flip bits
    ones = ''.join('1' if b == '0' else '0' for b in val)
    # Add 1
    return add(ones, '1')


def arithmetic_right_shift(A, Q, Q_1):
    combined = A + Q + Q_1
    shifted = combined[0] + combined[:-1]
    
    new_A = shifted[:len(A)]
    new_Q = shifted[len(A):len(A) + len(Q)]
    new_Q_1 = shifted[-1]
    
    return new_A, new_Q, new_Q_1


def booth_multiplication(multiplicand, multiplier):
    # Determine bit length required
    bit_len = max(multiplicand.bit_length(), multiplier.bit_length()) + 2
    
    # Convert to 2's complement binary representations
    if multiplicand < 0:
        M = complement(format((1 << bit_len) + multiplicand, f'0{bit_len}b'))[-bit_len:]
    else:
        M = format(multiplicand, f'0{bit_len}b')
        
    if multiplier < 0:
        Q = complement(format((1 << bit_len) + multiplier, f'0{bit_len}b'))[-bit_len:]
    else:
        Q = format(multiplier, f'0{bit_len}b')
        
    A = '0' * bit_len
    Q_1 = '0'
    M_neg = complement(M)[-bit_len:]
    
    print(f"Initial Values:")
    print(f"A: {A}, Q: {Q}, Q_-1: {Q_1}, M: {M}")
    print("-" * 40)
    
    for i in range(1, bit_len + 1):
        last_two = Q[-1] + Q_1
        
        if last_two == "10":
            A = add(A, M_neg)[-bit_len:]
            print(f"Step {i} (A = A - M): A={A}")
        elif last_two == "01":
            A = add(A, M)[-bit_len:]
            print(f"Step {i} (A = A + M): A={A}")
            
        A, Q, Q_1 = arithmetic_right_shift(A, Q, Q_1)
        print(f"Shift -> A: {A}, Q: {Q}, Q_-1: {Q_1}")
        
    product_binary = A + Q
    return product_binary


if __name__ == "__main__":
    try:
        num1 = int(input("Enter Multiplicand (Decimal): "))
        num2 = int(input("Enter Multiplier (Decimal): "))
        
        result_bin = booth_multiplication(num1, num2)
        print("-" * 40)
        print(f"Binary Product: {result_bin}")
    except ValueError:
        print("Please enter valid integers.")
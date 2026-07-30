def add(A, M):
    carry = 0
    Sum = ""
    for i in range(len(A) - 1, -1, -1):
        temp = int(A[i]) + int(M[i]) + carry
        Sum += str(temp % 2)
        carry = 1 if temp > 1 else 0
    return Sum[::-1]


def compliment(m):
    # Flip bits
    M = ''.join('1' if b == '0' else '0' for b in m)
    # Add 1 to get 2's complement
    one = '0' * (len(m) - 1) + '1'
    return add(M, one)


def nonRestoringDivision(dividend_dec, divisor_dec):
    # Convert decimal to binary and determine bit length
    # We add 1 extra bit for the sign bit to handle overflow/subtraction
    bit_len = max(dividend_dec.bit_length(), divisor_dec.bit_length()) + 1
    
    Q = format(dividend_dec, f'0{bit_len}b')
    M = format(divisor_dec, f'0{bit_len}b')
    A = '0' * bit_len
    comp_M = compliment(M)
    
    count = bit_len
    flag = 'successful'  # 'successful' means A was positive
    
    print(f"Initial Values: A:{A} Q:{Q} M:{M}")
    
    for i in range(1, bit_len + 1):
        print(f"\nStep {i}: ", end="")
        
        # Shift Left
        combined = A + Q
        combined = combined[1:]
        A = combined[:bit_len]
        Q_temp = combined[bit_len:]  # Q without the last bit yet
        
        if flag == 'successful':
            A = add(A, comp_M)
            print("Shift Left & Subtract")
        else:
            A = add(A, M)
            print("Shift Left & Add")
            
        if A[0] == '1':  # A is negative
            Q = Q_temp + '0'
            flag = 'unsuccessful'
        else:  # A is positive
            Q = Q_temp + '1'
            flag = 'successful'
            
        print(f"A: {A} | Q: {Q}")
        
    if A[0] == '1':
        print("\nFinal Step: A is negative, performing correction (A = A + M)")
        A = add(A, M)
        
    print("-" * 30)
    print(f"Binary Quotient: {Q} (Decimal: {int(Q, 2)})")
    print(f"Binary Remainder: {A} (Decimal: {int(A, 2)})")


if __name__ == "__main__":
    try:
        num1 = int(input("Enter Dividend (Decimal): "))
        num2 = int(input("Enter Divisor (Decimal): "))
        
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            nonRestoringDivision(num1, num2)
    except ValueError:
        print("Please enter valid integers.")
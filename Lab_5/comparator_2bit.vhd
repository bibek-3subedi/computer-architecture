library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity COMPARATOR_2BIT is
    port(
        A  : in std_logic_vector(1 downto 0);
        B  : in std_logic_vector(1 downto 0);
        EQ : out std_logic;
        GT : out std_logic;
        LT : out std_logic
    );
end entity COMPARATOR_2BIT;

architecture Dataflow of COMPARATOR_2BIT is
    -- Intermediate signals for readability (representing bit equality)
    signal eq1, eq0 : std_logic;
begin
    -- Check if individual bits are equal (XNOR logic)
    eq1 <= A(1) xnor B(1);
    eq0 <= A(0) xnor B(0);

    -- Combinational Logic Assignments
    EQ <= eq1 and eq0;
    
    GT <= (A(1) and not B(1)) or (eq1 and A(0) and not B(0));
    
    LT <= (not A(1) and B(1)) or (eq1 and not A(0) and B(0));

end architecture Dataflow;
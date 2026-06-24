library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity COMPARATOR_2BIT is
    port(
        A: in std_logic_vector(1 downto 0);
        B: in std_logic_vector(1 downto 0);
        EQ: out std_logic;
        GT: out std_logic;
        LT: out std_logic
    );
end entity COMPARATOR_2BIT;

architecture Behavioral of COMPARATOR_2BIT is
begin
    process(A,B)
    begin
        if unsigned(A)=unsigned(B) then
            EQ <= '1'; GT <= '0'; LT <= '0';
        elsif unsigned(A)>unsigned(B) then
            EQ <= '0'; GT <= '1'; LT <= '0';
        else
            EQ <= '0'; GT <= '0'; LT <= '1';
        end if;
    end process;
end architecture Behavioral;

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ENCODER_4TO2 is
port (
    I : in std_logic_vector(3 downto 0);   -- 4 inputs
    Y : out std_logic_vector(1 downto 0);  -- 2-bit output
    V : out std_logic                       -- Valid
);
end entity ENCODER_4TO2;

architecture Behavioral of ENCODER_4TO2 is
begin

process(I)
begin

    if I = "0000" then
        Y <= "00";
        V <= '0';

    elsif I(3) = '1' then
        Y <= "11";
        V <= '1';

    elsif I(2) = '1' then
        Y <= "10";
        V <= '1';

    elsif I(1) = '1' then
        Y <= "01";
        V <= '1';

    else
        Y <= "00";
        V <= '1';
    end if;

end process;

end architecture Behavioral;
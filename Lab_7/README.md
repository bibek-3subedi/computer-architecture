# Lab 7: VHDL Code for Sequential Circuits — Flip-Flops

---

## Objective

- Design and simulate SR, D, JK, and T flip-flops using VHDL.
- Examine the function of the clock signal in governing sequential circuit behavior.

---

## Theory

A flip-flop is a bistable sequential storage element capable of holding one bit of information. In contrast to combinational logic, a flip-flop's output is determined not only by its present inputs but also by its previously stored state. Each flip-flop examined in this lab is edge-triggered, responding specifically to the **rising edge** of the clock signal.

---

### SR Flip-Flop

The SR flip-flop is governed by two control inputs, Set (S) and Reset (R). Applying a logic HIGH to both inputs simultaneously produces an undefined, forbidden output state.

| S   | R   | Q (next)      |
| --- | --- | ------------- |
| 0   | 0   | Q (no change) |
| 0   | 1   | 0 (reset)     |
| 1   | 0   | 1 (set)       |
| 1   | 1   | X (forbidden) |

---

### D Flip-Flop

The D flip-flop transfers the logic value present at input D to its output on every rising clock edge, thereby resolving the ambiguity inherent in the SR flip-flop's forbidden state.

```
Q(next) = D
```

---

### JK Flip-Flop

The JK flip-flop refines the SR design by removing its undefined condition. Instead of producing an invalid output, asserting both J and K simultaneously causes the flip-flop to **toggle** its state.

```
Q(next) = J·Q' + K'·Q
```

| J   | K   | Q (next)      |
| --- | --- | ------------- |
| 0   | 0   | Q (no change) |
| 0   | 1   | 0 (reset)     |
| 1   | 0   | 1 (set)       |
| 1   | 1   | Q' (toggle)   |

---

### T Flip-Flop

The T (Toggle) flip-flop inverts its stored output whenever T is asserted, and retains its current state when T is de-asserted.

```
Q(next) = T ⊕ Q
```

| T   | Q (next)      |
| --- | ------------- |
| 0   | Q (no change) |
| 1   | Q' (toggle)   |

---

## Design Files

### 1. SR Flip-Flop

**Filename:** `sr_ff.vhd`

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity SR_FF is
    port (
        CLK : in  std_logic;
        S   : in  std_logic;
        R   : in  std_logic;
        Q   : out std_logic;
        QB  : out std_logic  -- Q complement
    );
end entity SR_FF;

architecture Behavioral of SR_FF is
    signal Q_int : std_logic := '0';
begin
    process (CLK)
    begin
        if rising_edge(CLK) then
            if    S = '0' and R = '0' then null;        -- Hold
            elsif S = '0' and R = '1' then Q_int <= '0'; -- Reset
            elsif S = '1' and R = '0' then Q_int <= '1'; -- Set
            -- S=1, R=1 is forbidden: no assignment
            end if;
        end if;
    end process;

    Q  <= Q_int;
    QB <= not Q_int;
end architecture Behavioral;
```

---

### 2. D Flip-Flop

**Filename:** `d_ff.vhd`

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity D_FF is
    port (
        CLK : in  std_logic;
        D   : in  std_logic;
        Q   : out std_logic;
        QB  : out std_logic
    );
end entity D_FF;

architecture Behavioral of D_FF is
    signal Q_int : std_logic := '0';
begin
    process (CLK)
    begin
        if rising_edge(CLK) then
            Q_int <= D;
        end if;
    end process;

    Q  <= Q_int;
    QB <= not Q_int;
end architecture Behavioral;
```

---

### 3. JK Flip-Flop

**Filename:** `jk_ff.vhd`

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity JK_FF is
    port (
        CLK : in  std_logic;
        J   : in  std_logic;
        K   : in  std_logic;
        Q   : out std_logic;
        QB  : out std_logic
    );
end entity JK_FF;

architecture Behavioral of JK_FF is
    signal Q_int : std_logic := '0';
begin
    process (CLK)
    begin
        if rising_edge(CLK) then
            if    J = '0' and K = '0' then null;              -- Hold
            elsif J = '0' and K = '1' then Q_int <= '0';      -- Reset
            elsif J = '1' and K = '0' then Q_int <= '1';      -- Set
            else                           Q_int <= not Q_int; -- Toggle
            end if;
        end if;
    end process;

    Q  <= Q_int;
    QB <= not Q_int;
end architecture Behavioral;
```

---

### 4. T Flip-Flop

**Filename:** `t_ff.vhd`

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity T_FF is
    port (
        CLK : in  std_logic;
        T   : in  std_logic;
        Q   : out std_logic;
        QB  : out std_logic
    );
end entity T_FF;

architecture Behavioral of T_FF is
    signal Q_int : std_logic := '0';
begin
    process (CLK)
    begin
        if rising_edge(CLK) then
            if T = '1' then
                Q_int <= not Q_int;  -- Toggle
            end if;
        end if;
    end process;

    Q  <= Q_int;
    QB <= not Q_int;
end architecture Behavioral;
```

---

## Testbench File

**Filename:** `ff_tb.vhd`

A unified testbench was developed to instantiate and exercise all four flip-flop designs concurrently. A continuous 20 ns-period clock is generated via a concurrent signal assignment. The stimulus process then applies input sequences to each flip-flop in turn, exercising every valid operating condition — Set, Reset, Hold, and Toggle — with each condition sustained for 40 ns (equivalent to two clock cycles) to guarantee reliable edge-triggered capture.

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity FF_TB is
end entity FF_TB;

architecture Simulation of FF_TB is
    signal CLK                          : std_logic := '0';
    signal S, R                         : std_logic := '0';
    signal D                            : std_logic := '0';
    signal J, K                         : std_logic := '0';
    signal T                            : std_logic := '0';
    signal Q_SR, Q_D, Q_JK, Q_T        : std_logic;
    signal QB_SR, QB_D, QB_JK, QB_T    : std_logic;

    constant CLK_PERIOD : time := 20 ns;
begin
    -- Clock generation
    CLK <= not CLK after CLK_PERIOD / 2;

    U1 : entity work.SR_FF port map (CLK, S, R, Q_SR, QB_SR);
    U2 : entity work.D_FF  port map (CLK, D, Q_D, QB_D);
    U3 : entity work.JK_FF port map (CLK, J, K, Q_JK, QB_JK);
    U4 : entity work.T_FF  port map (CLK, T, Q_T, QB_T);

    STIMULUS : process
    begin
        -- SR FF test
        S <= '1'; R <= '0'; wait for 40 ns;  -- Set
        S <= '0'; R <= '1'; wait for 40 ns;  -- Reset
        S <= '0'; R <= '0'; wait for 40 ns;  -- Hold

        -- D FF test
        D <= '1'; wait for 40 ns;
        D <= '0'; wait for 40 ns;

        -- JK FF test
        J <= '1'; K <= '0'; wait for 40 ns;  -- Set
        J <= '1'; K <= '1'; wait for 40 ns;  -- Toggle
        J <= '0'; K <= '1'; wait for 40 ns;  -- Reset

        -- T FF test
        T <= '1'; wait for 80 ns;  -- Toggle twice
        T <= '0'; wait for 40 ns;  -- Hold

        wait;
    end process;
end architecture Simulation;
```

### Simulation Commands

```bash
# 1. Analyze all design files and testbench
ghdl -a sr_ff.vhd d_ff.vhd jk_ff.vhd t_ff.vhd ff_tb.vhd

# 2. Elaborate the testbench
ghdl -e FF_TB

# 3. Simulate and export waveform
ghdl -r FF_TB --vcd=flipflops.vcd

# 4. Open waveform in GTKWave
gtkwave flipflops.vcd
```

---

## Simulation File

**Filename:** `flipflops.vcd`

This Value Change Dump file is produced by GHDL upon execution of the testbench. It captures every transition of the clock, input, and output signals for all four flip-flop instances throughout the simulation, and serves as the input source for visual verification within GTKWave.

---

## Output

The generated waveform was imported into GTKWave, where the clock signal along with all flip-flop input and output traces were added to the display and the view was zoomed to fit the full simulation window.

**Observation:** Each of the four flip-flops exhibited the expected behavior in response to its respective input conditions at every rising clock edge. The SR flip-flop performed set and reset operations correctly while never entering the forbidden state. The D flip-flop reliably captured the input value at each rising edge. The JK flip-flop toggled as expected under the J = K = 1 condition. The T flip-flop toggled on each rising edge while T remained asserted and held its state once T was de-asserted. In every case, the QB output remained the logical complement of Q.

---

## Discussion and Conclusion

This lab presented the design and verification of four fundamental sequential circuit building blocks — the SR, D, JK, and T flip-flops — implemented in VHDL using behavioral modeling. Each design relied on rising-edge clock triggering and an internal state signal to drive both the Q and QB outputs. Verification was carried out through a single integrated testbench featuring a generated clock and a sequential stimulus process covering all valid operating conditions for each device. The resulting GTKWave waveform confirmed correct functional behavior across all test cases, encompassing state retention, setting, resetting, and toggling. Through this exercise, a solid grounding in clocked sequential circuit design was established, providing the foundation necessary for constructing registers, counters, and finite state machines in the labs to follow.

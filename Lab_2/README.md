
# Lab 2:  VHDL Code for Realizing Logic Gates

## Objective

- Design and implement structural/behavioral VHDL code for all fundamental logic gates: AND, OR, NOT, NAND, NOR, XOR, and XNOR.
- Simulate the circuit behaviors and validate their corresponding truth tables using GTKWave.

---

## Theory and Mathematical Expressions

Logic gates serve as the foundational structural elements of modern digital systems. Each gate processes binary input variables to yield a deterministic single-bit output based on Boolean algebra.

| Gate Type | VHDL Operator |     Boolean Expression      |
| :-------- | :-----------: | :-------------------------: |
| AND       |     `and`     |       $Y = A \cdot B$       |
| OR        |     `or`      |         $Y = A + B$         |
| NOT       |     `not`     |        $Y = \bar{A}$        |
| NAND      |    `nand`     | $Y = \overline{A \cdot B}$  |
| NOR       |     `nor`     |   $Y = \overline{A + B}$    |
| XOR       |     `xor`     |      $Y = A \oplus B$       |
| XNOR      |    `xnor`     | $Y = \overline{A \oplus B}$ |

---

## Verification Truth Table

| Input A | Input B | AND | OR  | NOT A | NAND | NOR | XOR | XNOR |
| :-----: | :-----: | :-: | :-: | :---: | :--: | :-: | :-: | :--: |
|    0    |    0    |  0  |  0  |   1   |  1   |  1  |  0  |  1   |
|    0    |    1    |  0  |  1  |   1   |  1   |  0  |  1  |  0   |
|    1    |    0    |  0  |  1  |   0   |  1   |  0  |  1  |  0   |
|    1    |    1    |  1  |  1  |   0   |  0   |  0  |  0  |  1   |

---

## Simulation Output

The generated Value Change Dump (`.vcd`) file was visualized using GTKWave to confirm timing accuracy and signal transitions.

![Simulation Waveform](<Output.png>)

---

## Discussion and Analysis

The simulation waveform confirms correct logical operation across all test vectors. The stimulus process within the testbench systematically cycled through the four possible binary input combinations at uniform 10 ns intervals:

- **0 ns to 10 ns ($A = 0, B = 0$):** The output signals reflect the default states of the components. Compliant gates remain at logic low, while inverted functions (`NOT A`, `NAND`, `NOR`, `XNOR`) cleanly assert a logic high (`1`).
- **10 ns to 20 ns ($A = 1, B = 0$):** Upon the transition of input A to logic high, the `OR` and `XOR` outputs switch to `1`, while `NOT A` complements to logic low (`0`).
- **20 ns to 30 ns ($A = 0, B = 1$):** Inputs invert to evaluate asymmetric behavior. The outputs dynamically adapt, holding `OR` and `XOR` high while verifying the functional independence of the input lines.
- **30 ns onwards ($A = 1, B = 1$):** The final vector asserts logic high on both inputs. This triggers the `AND` and `XNOR` outputs to transition to logic high (`1`), while the `NAND` output drops to logic low (`0`).

---

## Conclusion

The VHDL code for all seven basic logic gates was successfully compiled, executed, and verified. By tracking the runtime waveform transitions inside the GTKWave environment, the functional behavioral integrity of the underlying hardware blocks was validated against theoretical Boolean models. This establishes a verified baseline for constructing complex combinational and sequential sub-systems in subsequent lab modules.


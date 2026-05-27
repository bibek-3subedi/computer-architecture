# Lab 3: VHDL Code for Combinational Circuits (Encoder and Decoder)

---

## Objective

- To design and simulate a **4-to-2 priority encoder** using VHDL.  
- To design and simulate a **2-to-4 decoder** using VHDL.  

---

## Theory

### Encoder

An encoder is a combinational logic circuit that converts \(2^n\) input lines into an **n-bit binary output**. At any instant, only one input is assumed to be active (HIGH).

A **4-to-2 encoder** consists of four inputs (I0–I3) and produces a 2-bit output (Y1, Y0).

A **priority encoder** is a modified encoder that resolves multiple active inputs by assigning priority to the highest-order input.

#### Truth Table (4-to-2 Priority Encoder)

| I3 | I2 | I1 | I0 | Y1 | Y0 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | X  | 0  | 1  |
| 0  | 1  | X  | X  | 1  | 0  |
| 1  | X  | X  | X  | 1  | 1  |

---

### Decoder

A decoder is a combinational circuit that performs the reverse operation of an encoder by converting an **n-bit binary input** into one of \(2^n\) output lines.

A **2-to-4 decoder** has a 2-bit input (A1, A0) and four outputs (Y0–Y3). At any time, only one output is active based on the input combination.

#### Truth Table (2-to-4 Decoder)

| A1 | A0 | Y3 | Y2 | Y1 | Y0 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 1  |
| 0  | 1  | 0  | 0  | 1  | 0  |
| 1  | 0  | 0  | 1  | 0  | 0  |
| 1  | 1  | 1  | 0  | 0  | 0  |

---

## Output

### Decoder Output
(<img width="1243" height="788" alt="decoder vcd" src="https://github.com/user-attachments/assets/cdf1d700-7b71-4d30-8cf3-57a006add74a" />)

### Encoder Output
(<img width="1250" height="780" alt="encoder vcd" src="https://github.com/user-attachments/assets/9a72c43e-c1f9-4c9e-99c0-0db1b392a17f" />
)

---

## Discussion

In this experiment, two combinational circuits were implemented using VHDL: a **priority encoder** and a **decoder**.

The priority encoder demonstrates how multiple inputs are resolved by prioritizing the highest active input, producing a valid binary output. The decoder converts binary input values into a single active output line.

Simulation results verified correct functionality:
- Encoder correctly handled input priority.
- Decoder correctly activated only one output per input combination.

---

## Conclusion

This lab helped in understanding the design and implementation of **combinational logic circuits using VHDL**.

We successfully:
- Designed a **4-to-2 priority encoder**
- Designed a **2-to-4 decoder**
- Verified outputs using simulation tools (GTKWave)

The experiment confirmed correct behavior of both circuits and strengthened the fundamentals of digital logic design.

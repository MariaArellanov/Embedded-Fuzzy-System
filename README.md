# Multi-criteria Fuzzy System Applied to Elderly Healthcare
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

This repository contains the implementation of the Master's Thesis project focused on intelligent health and wellbeing monitoring, developed at the **Tecnológico Nacional de México (TecNM) campus León** between 2019 and 2021. The system integrates **Multi-Criteria Group Decision Making (MCGDM)** algorithms and **Fuzzy Control Systems (FCS)** to evaluate health status through smart device data processing.

## Project Information

* **Institution:** Tecnológico Nacional de México, Campus León.
* **By: María Arellano** - *Main Developer & Researcher*
* **Thesis Advisor:** Dr. Víctor Manuel Zamudio Rodríguez.
* **Publication 1:** [Design and Implementation of a Embedded Fuzzy Multi-criteria Group Decision Making System for Wellbeing, Health and Security](https://ieeexplore.ieee.org/document/9486555) (Published in IEEE Xplore).
* **Publication 2:** [Design of a Smart Device with Fuzzy Multi-criteria Group Decision Making System for The Elderly](https://ieeexplore.ieee.org/document/9486555) (Published in IEEE Xplore).


\---

## Software Structure

The code is organized into modular Python classes to separate decision logic from membership function definitions:

* **`main\_vf.py`**: The entry point of the application. It runs the complete workflow for both MCGDM and FCS algorithms.
* **`FCS.py`**: Class containing the **Fuzzy Control System** logic.
* **`MCGDM.py`**: Implementation of the **Multi-Criteria Group Decision Making** algorithm.
* **`Wellbeing.py`**: Defines variables and Membership Functions (MF) for parameters monitored under the **Wellbeing** category.
* **`Health.py`**: Defines variables and Membership Functions (MF) for parameters monitored under the **Health** category.
* **`grid.py`**: Utility file used to generate grids and visualizations for the final result analysis.

\---

## Hardware and Modeling

In addition to the computational logic, this project includes the modeling for a **Smart Device**. The system is designed to interface with hardware capable of collecting vital signs, enabling real-time evaluation based on the implemented fuzzy logic.

\---

## Getting Started

1. **Clone the repository:**

&#x20;   ```bash
    git clone https://github.com/MariaArellanov/Embedded-Fuzzy-System.git
    ```

2. **Prerequisites:**
The system requires Python 3.x and the following libraries:

&#x20;   ```bash
    pip install numpy scikit-fuzzy matplotlib
    ```

3. **Run the simulation:**

&#x20;   ```bash
    python main\_vf.py
    ```

\---
## Citation
If you use this software in your research, please cite it as follows:
```bibtex
@software{Arellano_Embedded_MCGDM_System_2021,
  author = { M. Arellano, V. M. Zamudio, et al.},
  title = {Monitoring Patients Using Intelligent Agents: A MAS Approach},
  year = {2021},
  publisher = {Zenodo}
}

\---

*Research focused on the application of Intelligent Systems to improve quality of life.*


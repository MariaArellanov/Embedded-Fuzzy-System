# Embedded-Fuzzy-System
Multi-criteria Fuzzy System Applied to Elderly Healthcare
This repository contains the implementation of the Master's Thesis project focused on intelligent health and wellbeing monitoring, developed at the Tecnológico Nacional de México (TecNM) campus León between 2019 and 2021. The system integrates Multi-Criteria Group Decision Making (MCGDM) algorithms and Fuzzy Control Systems (FCS) to evaluate health status through smart device data processing.
Project Information
Institution: Tecnológico Nacional de México, Campus León.
Thesis Advisor: Dr. Víctor Manuel Zamudio Rodríguez.
Publication: Multi-criteria and Fuzzy Logic System for Health and Wellbeing Monitoring (Published in IEEE Xplore).
---
Software Structure
The code is organized into modular Python classes to separate decision logic from membership function definitions:
`main_vf.py`: The entry point of the application. It runs the complete workflow for both MCGDM and FCS algorithms.
`FCS.py`: Class containing the Fuzzy Control System logic.
`MCGDM.py`: Implementation of the Multi-Criteria Group Decision Making algorithm.
`Wellbeing.py`: Defines variables and Membership Functions (MF) for parameters monitored under the Wellbeing category.
`Health.py`: Defines variables and Membership Functions (MF) for parameters monitored under the Health category.
`grid.py`: Utility file used to generate grids and visualizations for the final result analysis.
---
Hardware and Modeling
In addition to the computational logic, this project includes the modeling for a Smart Device. The system is designed to interface with hardware capable of collecting vital signs, enabling real-time evaluation based on the implemented fuzzy logic.
---
Getting Started
Clone the repository:
    ```bash
    git clone https://github.com/your-username/fuzzy-health-system.git
    ```
Prerequisites:
The system requires Python 3.x and the following libraries:
    ```bash
    pip install numpy scikit-fuzzy matplotlib
    ```
Run the simulation:
    ```bash
    python main_vf.py
    ```
---
Citation
If you use this code or the methodology in your research, please cite the original paper:
> M. Arellano, V. M. Zamudio, et al., "Multi-criteria and Fuzzy Logic System for Health and Wellbeing Monitoring," 2021. [IEEE Xplore].
---
Research focused on the application of Intelligent Systems to improve quality of life.

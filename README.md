# load_DG_DATA

Description

The load_DG_DATA repository contains code for loading and analyzing data related to active and reactive powers of various loads in distribution grids, as well as data from distributed generation (DG) sources such as wind turbines (WT) and photovoltaic (PV) systems.

General Data (python)

The repository includes general data related to distribution systems, which provides information about the overall structure and characteristics of the grids. Additionally, it contains time series data for the active and reactive powers of 34 different loads in the distribution grids. These load data are based on a 15-minute resolution and accurately reflect the real consumption and generation patterns of the devices.

P2P Market Data (MATLAB)

The repository also contains data related to peer-to-peer (P2P) energy markets. This dataset provides time series data on the behavior of households within low voltage distribution grids. It offers insights into how energy is traded and consumed within these markets. Furthermore, the repository provides the scaled output of PV units as an average output over a year. For daily PV output values, please refer to the following link: https://www.renewables.ninja.

Usage

The code in this repository allows users to load and manipulate the aforementioned data for analysis and modeling purposes. It provides functions and scripts for accessing and processing the data efficiently.

Dependencies

The code relies on the following dependencies:

Python 3.x
NumPy
Pandas
Matplotlib
Please ensure that these dependencies are installed in your environment before running the code.
--
Matlab

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Please cite the data by using the following reference: will be updates

Thank you for using load_DG_DATA!

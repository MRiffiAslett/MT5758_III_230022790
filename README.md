# MT5758 Assignment 3: Exploring Global Socio-Economic Patterns

## Introduction
This project aims to identify predominant socio-economic patterns and groupings among the world's nations. It involves a comprehensive analysis of various socio-economic indicators using multivariate methods such as Multidimensional Scaling (MDS) and K-means clustering. The study focuses on data post-COVID-19 to understand emerging trends and disparities.

## Repository Structure
- `README.md`: This file, explaining the project and repository.
- `Country-data.csv.xls`: The main dataset containing socio-economic indicators.
- `Corr_continent_country_data.csv`: Extended dataset with continent and coordinates.
- `MT5758 Assignment III.qmd`: R code and documentation for data analysis.
- `Python_script_Coordinates_and_continent_append.py`: Python script to append coordinates and continent data.
- `Python_script_K_means_different_distance_measures.py`: Python script for K-means clustering with various distance measures.
- `Python_script_Create_Maps.py`: Python script for creating visualizations of the data.
- `/Plots/`: Directory containing generated plots and visualizations.

## Installation and Usage
To run the scripts and reproduce the analysis, ensure you have R and Python installed with the necessary libraries.

### R Dependencies
- `dplyr`
- `ggplot2`
- `gridExtra`
- `corrplot`
- `magick`
- `GGally`
- `knitr`
- `markdown`
- `readr`
- `RColorBrewer`
- `tidyr`

### Python Dependencies
- `pandas`
- `geopandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

Run the R scripts in the order presented in `MT5758 Assignment III.qmd` for a step-by-step analysis.

## Project Findings
The project uncovers various socio-economic clusters among nations post-COVID-19. Key findings include:
- Distinct socio-economic disparities based on geographical regions.
- Significant correlation between socio-economic factors like fertility rate and child mortality.
- The effectiveness of Euclidean and Manhattan distances in clustering nations based on socio-economic factors.

Visualizations and in-depth analyses are detailed within the R markdown document.

## Acknowledgments
Special thanks to the University of St-Andrews and the School of Mathematics and Statistics for guidance and resources. Appreciation to Laila Qadir Musib for compiling the initial dataset.

---

*This README was generated with the assistance of an AI language model.*

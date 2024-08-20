# Results Documentation 

## Introduction

The `network_spatial_coherence` package processes graph data and generates comprehensive results that are organized into specific directories. Modify the `GraphArgs` configuration to change which results are being computed!

### Directory Structure Overview

```plaintext
network_spatial_coherence/
│
├── data/
│   ├── edge_lists/               # CSV files: source, target, weight
│   ├── original_positions/       # Original positions of nodes
│   ├── reconstructed_positions/  # Positions after reconstruction
│   ├── colorcode/                # Files for coloring nodes or edges
│   └── network_json_format/      # Network data in JSON format
│
└── results/
    ├── output_dataframe/         # Spatial Coherence results among other graph properties
    ├── plots/                    # General plots generated from analyses
    │   ├── original_image/        # Plots of the original graph representations
    │   ├── reconstructed_image/   # Plots showing reconstructed graph representations
    └── spatial_coherence_plots/  # Main spatial coherence results
```

## Understanding the Results

### Output DataFrame

Located in `results/output_dataframe/`, this directory contains CSV files that are generated in each run. Each file is a DataFrame detailing the results from each analysis run, including:

- Graph properties
- Metrics calculated during the analysis (such as spatial coherence)
- Summary statistics

### Spatial Coherence Plots

Visualizations are crucial for understanding the network's spatial coherence. Find these plots in
These include:

- **Original Image Plots**: Show the original graph as provided. Mostly useful for simulations where ground truth is available.
- **Reconstructed Image Plots**: Show the reconstructed network, if reconstruction is set to True.
- **Spatial Constant Plots**: Stability of spatial constant
- **Dimension Prediction Plots**: Network dimension fits
- **Gram Matrix Analysis**: Eigenvalue (variance) contribution for the Gram Matrix, derived from the distance matrix.
Plots are saved in formats like SVG, PNG, or PDF, depending on your configuration settings.





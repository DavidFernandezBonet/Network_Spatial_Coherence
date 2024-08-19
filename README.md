# Network Spatial Coherence
Python library to validate the spatial coherence of a network. It offers tools to analyze network properties, check how "Euclidean" the network is (spatial coherence), and to reconstruct the network. Networks can be both simulated (e.g. a KNN network) or imported.

## Features
- Analyze the spatial coherence of a network
- Reconstruction images from purely network information
- Efficient graph loading and processing (using sparse matrices or getting a graph sample)


## Install
Python 3.11 is reccomended, although older versions should work.

```bash
pip install git+https://github.com/DavidFernandezBonet/Spatial_Constant_Analysis.git
```
If you require authentication you can use a PAT (a github token) instead. Go to Developer settings > Personal access tokens > Generate new token and then save the token because it will not be displayed again. You should input it in this line of code
```bash
pip install git+https://<token>:x-oauth-basic@github.com/DavidFernandezBonet/Spatial_Constant_Analysis.git
```
## Usage
For a detailed tutorial, see the [Jupyter Notebook Tutorial](./network_spatial_coherence/network_spatial_coherence_tutorial.ipynb) in this repository.

1. Access documentation for detailed API usage:

```python
from network_spatial_coherence.docs_util import access_docs
access_docs()
```

2. Minimum working example

```python
from network_spatial_coherence import nsc_pipeline
from network_spatial_coherence import structure_and_args
structure_and_args.create_project_structure()
graph, args = nsc_pipeline.load_and_initialize_graph()
nsc_pipeline.run_pipeline(graph, args)
```



## Contact
[dfb@kth.se]



## Directory Structure

The `network_spatial_coherence` package organizes its files within two main directories: `data` and `results`, facilitating easy management of input data and output results.

### Data
The `data` directory is intended for all input files needed to run analyses. It is structured as follows:
- **Edge Lists** (`data/edge_lists`): Place your edge list files here. Edge lists should be in CSV format with columns `source`, `target`, `weight`.
- **Original Positions** (`data/original_positions`): Store original positions of nodes if available.
- **Reconstructed Positions** (`data/reconstructed_positions`): This folder will contain the positions after running reconstruction algorithms.
- **Color Codes** (`data/colorcode`): Optional directory for storing files that help in coloring nodes or edges in plots.
- **JSON Formats** (`data/network_json_format`): Store network data in JSON format here.

### Results
The `results` directory stores outputs generated from the analyses, including data frames and plots:
- **Output DataFrame** (`results/output_dataframe`): Contains comprehensive results in DataFrame format.
- **Plots**:
  - Main plots (`results/plots`): General plots generated from analyses.
  - Original Images (`results/plots/original_image`): Plots of the original graph representations.
  - Reconstructed Images (`results/plots/reconstructed_image`): Plots showing reconstructed graph representations.
  - Spatial Coherence (`results/spatial_coherence_plots`): Visualizations specifically for analyzing spatial coherence.
- **Detailed Analyses**:
  - Spatial Constants (`results/plots/spatial_constant`): Includes sub-directory for subgraph sampling and thresholding analyses.
  - Dimension Predictions (`results/plots/predicted_dimension`): Includes local dimension plots, heatmaps of dimensions, and multi-iteration dimension predictions.
- **Statistical Distributions**:
  - Degree, Clustering Coefficients, Shortest Paths, and Weight Distributions are located under their respective directories in `results/plots`.
- **Profiler Outputs** (`results/plots/profiler`): Performance profiling outputs.

### Subgraph Analyses
For more detailed subgraph-level analysis, refer to:
- **All Subgraphs Reconstruction** (`results/plots/all_subgraphs_reconstruction`): Includes reconstructed positions and images for each subgraph analyzed.

This structured approach ensures that data management is intuitive and results are easily accessible for further analysis or reporting.



## Installation

To install `network_spatial_coherence`, run the following command:

```bash
pip install network_spatial_coherence
```


## Tree diagram
network_spatial_coherence/
│
├── data/
│ ├── edge_lists/ # CSV files: source, target, weight
│ ├── original_positions/ # Original positions of nodes
│ ├── reconstructed_positions/ # Positions after reconstruction
│ ├── colorcode/ # Files for coloring nodes or edges
│ └── network_json_format/ # Network data in JSON format
│
└── results/
├── output_dataframe/ # Comprehensive results in DataFrame format
├── plots/ # General plots generated from analyses
│ ├── original_image/ # Plots of the original graph representations
│ ├── reconstructed_image/ # Plots showing reconstructed graph representations
│ └── spatial_coherence_plots/ # Visualizations for analyzing spatial coherence
├── spatial_constant/ # Spatial constants analyses
│ ├── subgraph_sampling/ # Subgraph sampling analyses
│ └── weighted_threshold/ # Threshold analyses
└── predicted_dimension/ # Dimension predictions
├── local_dimension/ # Local dimension plots
├── heatmap_local_dimension/ # Heatmap of dimensions
└── several_predictions/ # Multi-iteration dimension predictions

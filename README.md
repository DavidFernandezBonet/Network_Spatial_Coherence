# Network Spatial Coherence
How spatially coherent is your network? This package, network spatial coherence, answers the question by checking how Euclidean the network is - how close it is to a physical network.
We do this by measuring 3 different properties. The network can also be reconstructed approximately to its original positions using the STRND algorithm. 
Networks can be both simulated (if you do not have a network, imported (your network!) and weighted (if you know the strength of pairwise interactions). 

## Features
- Analyze the spatial coherence of a network
- Reconstruction images from purely network information
- Efficient graph loading and processing (using sparse matrices or getting a graph sample)
- Handles simulated graphs, custom graphs, unweighted graphs, weighted graphs


## Install
Python 3.11 is reccomended, although older versions should work.

```bash
pip install network_spatial_coherence
```

## Usage
For a detailed tutorial, see the [Jupyter Notebook Tutorial](./network_spatial_coherence/network_spatial_coherence_tutorial.ipynb) in this repository.

1. Access documentation for detailed API usage:

```python
from network_spatial_coherence.docs_util import access_docs
access_docs()
```

2. Example run

```python
import network_spatial_coherence.nsc_pipeline as nsc
from network_spatial_coherence.structure_and_args import GraphArgs

args = GraphArgs()
# define conditions for the run
args.spatial_coherence_validation['gram_matrix'] = True
args.spatial_coherence_validation['network_dimension'] = False
args.spatial_coherence_validation['spatial_constant'] = False

args.show_plots = True
args.colorfile = "dna_cool2.png"
args.plot_original_image = True
args.reconstruct = True
args.reconstruction_mode = 'STRND'
args.plot_reconstructed_image = True
# ---------

# create or load the graph
graph, args = nsc.load_and_initialize_graph(args=args)
# run spatial coherence for the graph, with optional reconstruction
single_graph_args, output_df = nsc.run_pipeline(graph, args)
# results are stored in a dataframe
print(output_df)
```

3. Using custom (your own!) graphs
Before using your own graph, make sure the edge list is in the 'data/edge_lists' directory.
```python
args.proximity_mode = "experimental"
args.edge_list_title = "your_graph_edge_list.csv"
graph, args = nsc.load_and_initialize_graph(args=args)
single_graph_args, output_df = nsc.run_pipeline(graph, args)
```
```


## Directory structure

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
    
- **Edge Lists** (`data/edge_lists`): Place your edge list files here. This is the only input needed if you want to run your own data, but make sure to set "args.proximity_mode="experimental"". Edge lists should be in CSV format with columns `source`, `target`, `weight` (weight is optional).


## GraphArgs Configuration

`GraphArgs` provides a comprehensive set of configuration options to tailor the behavior of the network spatial coherence analysis. Below are detailed explanations of the key parameters you can adjust:

### General Settings

- **proximity_mode**: Defines the method used to determine node proximity in the graph. Available options include:
  - `knn`: k-nearest neighbors
  - `knn_bipartite`: k-nearest neighbors in a bipartite graph
  - `epsilon-ball`: Nodes within a specified epsilon distance
  - `epsilon_bipartite`: Epsilon distance in a bipartite graph
  - `lattice`
  - `delaunay_corrected`
  - `distance_decay`
  - `experimental`: Use experimental settings specific to your dataset
- **dim**: The dimensionality of the space for the graph (default is 2).
- **false_edges_count**: Number of false edges to simulate in the graph; useful for robustness testing (default is 0).
- **true_edges_deletion_ratio**: Proportion of true edges to delete randomly; for testing graph robustness (default is 0).
- **colorfile**: Path to an image file or a color code CSV to apply custom color schemes to the graph plots. Examples include:
  - `colorful_spiral.jpeg`
  - `colored_squares.png`
  - `dna.jpg`
  - `dna_cool2.png`
  - `color_gradient.jpg`
  - `weinstein_colorcode_february_corrected.csv`
  - `None` for no color file.
- **plot_graph_properties**: Set to `True` to enable plotting of graph properties; otherwise, set to `False`.
- **show_plots**: Enables the display of plots if set to `True`.
- **format_plots**: Defines the format of the output plots. Options are `svg`, `pdf`, or `png`.

### Performance and Reconstruction Settings

- **large_graph_subsampling**: If `True`, subsamples large graphs to a maximum of 3000 nodes to save on processing time and memory.
- **max_subgraph_size**: Sets the maximum number of nodes in a subgraph when subsampling (default is 4000).
- **reconstruct**: Enables graph reconstruction if set to `True`.
- **reconstruction_mode**: Selects the algorithm for graph reconstruction. Options include:
  - `STRND`
  - `ggvec`
  - `landmark_isomap`
  - `PyMDE`
  - `MDS`

### Graph Analysis Settings

- **spatial_coherence_validation**: A dictionary containing settings for validating spatial coherence:
  - `spatial_constant`: Enables spatial constant validation.
  - `network_dimension`: Validates dimensions of the network.
  - `gram_matrix`: Uses a Gram matrix for validation.
- **community_detection**: Enable community detection within the graph if set to `True`.
- **handle_all_subgraphs**: If `True`, processes all identified subgraphs.
- **plot_original_image**: Enable plotting of the original graph images.
- **plot_reconstructed_image**: Enable plotting of reconstructed graph images.

### Weight and Distance Settings

- **weighted**: Set to `True` to consider the graph as weighted.
- **weight_threshold**: Sets the threshold for considering weights in the analysis.
- **weight_to_distance**: Converts weights to distances if `True`.
- **weight_to_distance_fun**: Function to convert weights to distances. Implementations might include `exp` for an exponential conversion.

### Simulation Specific Settings

- **num_points**: Number of points/nodes in the simulation.
- **intended_av_degree**: Intended average degree in the graph.
- **L**: System size or scale of the simulation space.
- **max_false_edge_length**: Maximum length of false edges; used to control simulation accuracy.
- **point_mode**: Shape of the area used for point generation. Options include `circle`, `square`, `triangle`, `star`, `ring`.
- **density_anomalies**: If `True`, introduces anomalies in point density.

### Experimental Scenario Settings

- **edge_list_title**: Specifies the title of the edge list file to use.
- **original_positions_available**: Set to `True` if original positions are available in the dataset.

This comprehensive set of parameters allows users to finely control the execution and characteristics of their network spatial coherence analysis.




## Contact
[dfb@kth.se]

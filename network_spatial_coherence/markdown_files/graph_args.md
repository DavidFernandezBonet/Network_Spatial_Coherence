
## GraphArgs Configuration

`GraphArgs` provides a set of configuration options to modify behavior of the network spatial coherence analysis. Details below:

### General Settings

- **proximity_mode**: Defines the method used to determine node proximity in the graph. Available options include:
  - `knn`: k-nearest neighbors
  - `knn_bipartite`: k-nearest neighbors in a bipartite graph
  - `epsilon-ball`: Nodes within a specified epsilon distance
  - `epsilon_bipartite`: Epsilon distance in a bipartite graph
  - `lattice`: square or cubic lattice
  - `delaunay_corrected`: voronoi/delaunay cells
  - `distance_decay`: connection modeling diffusion
  - `experimental`: Use experimental settings specific to your own dataset
- **dim**: The dimensionality of the space for the graph (default is 2).
- **false_edges_count**: Number of false edges to simulate in the graph; useful for robustness testing (default is 0). 
- **true_edges_deletion_ratio**: Proportion of true edges to delete randomly; for testing graph robustness (default is 0). It simulates missing edges.
- **colorfile**: Path to an image file or a color code CSV to apply custom color schemes to the graph plots. Examples include: (but you can make your own with a simple png file)
  - `dna_cool2.png`
  - `None` for no color file.
- **plot_graph_properties**: Set to `True` to enable plotting of graph properties; otherwise, set to `False`.
- **show_plots**: Enables the display of plots if set to `True`.
- **format_plots**: Defines the format of the output plots. Options are `svg`, `pdf`, or `png`.

### Performance and Reconstruction Settings

- **large_graph_subsampling**: If `True`, subsamples large graphs to a maximum of 3000 nodes to save on processing time and memory.
- **max_subgraph_size**: Sets the maximum number of nodes in a subgraph when subsampling (default is 4000).
- **reconstruct**: Enables graph reconstruction if set to `True`.
- **reconstruction_mode**: Selects the algorithm for graph reconstruction. Options include:
  - `STRND`: better reconstruction robustness for spatial incoherence
  - `landmark_isomap`


### Graph Analysis Settings

- **spatial_coherence_validation**: A dictionary containing settings for validating spatial coherence:
  - `spatial_constant`: If `True`, enables spatial constant computation (careful, can be computationally demanding).
  - `network_dimension`: If `True`, computes network dimension
  - `gram_matrix`: If `True`, omputes Gram Matrix eigenvalues and its analysis.
- **handle_all_subgraphs**: If `True`, processes all identified subgraphs. Useful for disconnected graphs only.
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
- **max_false_edge_length**: Maximum length of false edges; used to limit the distance where false edges can connect.
- **point_mode**: Shape of the area used for point generation. Options include `circle`, `square`.

### Experimental Scenario Settings

- **edge_list_title**: Specifies the title of the edge list file to use.
- **original_positions_available**: Set to `True` if original positions are available in the dataset. For custom postitions, make sure they are available in the data/positions folder.



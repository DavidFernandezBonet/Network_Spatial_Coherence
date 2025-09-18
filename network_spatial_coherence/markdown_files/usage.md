# Usage


## Example run

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

## Using custom (your own!) graphs
Before using your own graph, make sure the edge list is in the 'data/edge_lists' directory.
```python
args.proximity_mode = "experimental"
args.edge_list_title = "your_graph_edge_list.csv"
graph, args = nsc.load_and_initialize_graph(args=args)
single_graph_args, output_df = nsc.run_pipeline(graph, args)
```

## Fast Gram Matrix eigenvalues computation
```python
import network_spatial_coherence.nsc_pipeline as nsc
from network_spatial_coherence.structure_and_args import GraphArgs
import pandas as pd

args = GraphArgs()
args.proximity_mode = "experimental"
args.edge_list_title = "your_graph_edge_list.csv"
args.spatial_coherence_validation['gram_matrix'] = False
args.spatial_coherence_validation['network_dimension'] = False
args.spatial_coherence_validation['spatial_constant'] = False
args.spatial_coherence_validation['fast_gram_matrix'] = True
# For even faster results, run: args.spsatial_coherence_validation['sample_gram_matrix'] = True
# You can select the sample size with: args.max_subgraph_size = 4000

args.plot_original_image = False
args.reconstruct = False
args.plot_reconstructed_image = False

graph, args = nsc.load_and_initialize_graph(args=args)
single_graph_args, output_df = nsc.run_pipeline(graph, args)

# Make pandas show everything
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.colheader_justify", "center")
print(output_df.to_string(index=False))
```

## Access documentation for detailed API usage:

```python
from network_spatial_coherence.docs_util import access_docs
access_docs()
```

# Usage

## Quick Start: Minimal Working Example (5–10 seconds)
This example runs the full pipeline on a small bundled test network and verifies
that the installation is working correctly.

### Step 1: Install

    pip install network_spatial_coherence

### Step 2: Run the built-in example

    python -m network_spatial_coherence.examples.minimal_example

### Expected output

The script prints a summary table and creates a temporary working directory,
for example:

    /tmp/nsc_minimal_example_run/

containing:

    results/output_dataframe/
    results/spatial_coherence_plots/
    results/plots/

### Expected runtime

Typical runtime: **5–15 seconds** on a standard laptop.


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

## Speed Increase: Fast Gram Matrix Eigenvalues Computation

This example shows how to speed up Gram Matrix eigenvalue computation using the `network_spatial_coherence` library.  
It includes optional settings for sampling and faster execution.

### Setup and Configuration

```python
import network_spatial_coherence.nsc_pipeline as nsc
from network_spatial_coherence.structure_and_args import GraphArgs
import pandas as pd

args = GraphArgs()
args.proximity_mode = "experimental"
args.edge_list_title = "your_graph_edge_list.csv"

# Enable only the fast Gram Matrix computation
args.spatial_coherence_validation['gram_matrix'] = False
args.spatial_coherence_validation['network_dimension'] = False
args.spatial_coherence_validation['spatial_constant'] = False
args.spatial_coherence_validation['fast_gram_matrix'] = True

# Optional: sample-based computation for more speed
# args.spatial_coherence_validation['sample_gram_matrix'] = True
# args.max_subgraph_size = 4000

# Optional: multiple sampled runs --> Outputs mean and std deviation over samples
# args.spatial_coherence_validation['sample_gram_matrix_multiple']['enabled'] = True
# args.spatial_coherence_validation['sample_gram_matrix_multiple']['num_samples'] = 10
# args.spatial_coherence_validation['sample_gram_matrix_multiple']['sample_size'] = 1000

# Disable plotting for faster runs
args.plot_original_image = False
args.reconstruct = False
args.plot_reconstructed_image = False
```

---

### Running and Viewing Results

```python
graph, args = nsc.load_and_initialize_graph(args=args)
single_graph_args, output_df = nsc.run_pipeline(graph, args)

# Display all results clearly
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

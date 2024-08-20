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




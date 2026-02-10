from __future__ import annotations

import time
from pathlib import Path
from importlib.resources import files, as_file

import network_spatial_coherence.nsc_pipeline as nsc
from network_spatial_coherence.structure_and_args import GraphArgs


def main() -> None:
    # Create a deterministic temp run directory
    run_root = Path("/tmp/nsc_minimal_example_run")
    edge_dir = run_root / "data" / "edge_lists"
    edge_dir.mkdir(parents=True, exist_ok=True)

    # Locate packaged example edge list and copy into data/edge_lists/
    pkg_edge = files("network_spatial_coherence.examples").joinpath(
        "data/minimal_edge_list.csv"
    )
    with as_file(pkg_edge) as edge_path:
        target = edge_dir / "minimal_edge_list.csv"
        target.write_bytes(Path(edge_path).read_bytes())

    # Configure args to use this staged edge list
    args = GraphArgs(data_dir=str(run_root))
    args.proximity_mode = "experimental"
    args.edge_list_title = "minimal_edge_list.csv"
    args.dim = 2

    # Keep it fast and robust for reviewers
    args.show_plots = False
    args.reconstruct = False
    args.plot_original_image = False
    args.plot_reconstructed_image = False

    # Choose a path that is representative but fast.
    # (You can switch to gram_matrix=True if you prefer, but this is "time-to-first-result".)
    args.spatial_coherence_validation["gram_matrix"] = True
    args.spatial_coherence_validation["network_dimension"] = True
    args.spatial_coherence_validation["spatial_constant"] = True
    args.spatial_coherence_validation["fast_gram_matrix"] = False

    # Optional: demonstrate the fixed nested config (safe now that defaults exist)
    args.spatial_coherence_validation["sample_gram_matrix_multiple"]["enabled"] = False
    args.spatial_coherence_validation["sample_gram_matrix_multiple"]["num_samples"] = 2
    args.spatial_coherence_validation["sample_gram_matrix_multiple"][
        "sample_size"
    ] = 100

    print(f"[minimal_example] Run directory: {run_root}")
    print(f"[minimal_example] Edge list staged at: {target}")

    t0 = time.time()
    graph, args = nsc.load_and_initialize_graph(args=args)
    single_graph_args, output_df = nsc.run_pipeline(graph, args)
    dt = time.time() - t0

    print(f"[minimal_example] Completed in {dt:.2f} seconds")
    print("[minimal_example] Output preview:")
    print(output_df.head())

    # Tell the reviewer exactly where outputs go
    results_dir = run_root / "results"
    print(f"[minimal_example] Results directory: {results_dir}")
    print("[minimal_example] Key subfolders:")
    for p in [
        "output_dataframe",
        "spatial_coherence_plots",
        "plots",
        "main_spatial_coherence_plots",
    ]:
        pp = results_dir / p
        if pp.exists():
            print(f"  - {pp}")


if __name__ == "__main__":
    main()

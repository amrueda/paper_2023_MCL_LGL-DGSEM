# Trixi simulations

This repository contains code and instructions to reproduce the numerical
experiments reported in the article

> Monolithic Convex Limiting for Legendre-Gauss-Lobatto Discontinuous Galerkin Spectral Element Methods

The results were obtained using Julia v1.8.3 and [this version of Trixi.jl](https://github.com/bennibolm/Trixi.jl/tree/09f4dd77bb8d9cf797a6f9bcd71733f7cda5d64a). When this reproducibility repository was last updated, the implementation of FCT and MCL was not yet merged into the main [Trixi.jl](https://github.com/trixi-framework/Trixi.jl/) repository.

## Instructions

To run the examples, follow the instructions:

* Move to this directory and clone the Benjamin's fork of Trixi.jl repository:
  ```bash
  git clone git@github.com:bennibolm/Trixi.jl.git
  ```
* Move to the Trixi.jl folder and change to the branch where MCL is implemented:
  ```bash
  cd Trixi.jl
  git checkout 09f4dd7
  ```
* Install all the dependencies of Trixi.jl:
  ```bash
  cd Trixi.jl
  julia --project=@. -e 'import Pkg; Pkg.instantiate()' # Install Trixi's dependencies
  julia -e 'import Pkg; Pkg.add(["Trixi2Vtk", "Plots"])' # Install postprocessing tools
  julia -e 'import Pkg; Pkg.add("OrdinaryDiffEq")' # Install time integration schemes
  ```
* Run the individual examples using julia, e.g.,
  ```bash
  julia --check-bounds=no --threads=10 -e 'include(joinpath("..", "astrojet", "mcl_densityforall_pressureKuzminExact_cfl0.9_entropy_sequential", "elixir.jl"))'
  ```
* The simulation files will be stored in separate output folders. To visualize with paraview use Trixi2Vtk, e.g.,:
  ```bash
  julia --check-bounds=no --threads=10 -e 'using Trixi2Vtk ; trixi2vtk(joinpath("..", "astrojet", "mcl_densityforall_pressureKuzminExact_cfl0.9_entropy_sequential", "out87381", "solution_010284.h5"), output_directory="out")'
  ```
* To visualize the limiting factor fields, you will need to use [this version of Trixi2Vtk](https://github.com/bennibolm/Trixi2Vtk.jl/tree/2f0fb880789100ba09dcf0797200c86b893d1ac7).

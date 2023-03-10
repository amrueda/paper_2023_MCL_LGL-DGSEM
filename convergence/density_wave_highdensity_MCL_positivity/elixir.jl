
using OrdinaryDiffEq
using Trixi

###############################################################################
# semidiscretization of the compressible Euler equations
gamma = 1.4
equations = CompressibleEulerEquations2D(gamma)

include(joinpath(@__DIR__,"..","initial_condition_high_density.jl"))


initial_condition = initial_condition_density_wave_highdensity

surface_flux = flux_lax_friedrichs # HLLC needs more shock capturing (alpha_max)
volume_flux  = flux_ranocha # works with Chandrashekar flux as well
polydeg = 3
basis = LobattoLegendreBasis(polydeg)

# shock capturing necessary for this tough example
indicator_sc = IndicatorMCL(equations, basis;
                            DensityLimiter=false,
			    DensityAlphaForAll=false,
			    SequentialLimiter=false,
			    ConservativeLimiter=false,
			    DensityPositivityLimiter=true,
			    PressurePositivityLimiterKuzmin=true, 
			    IDPCheckBounds=true,
                            Plotting=true)
volume_integral=VolumeIntegralShockCapturingSubcell(indicator_sc; volume_flux_dg=volume_flux,
                                                                  volume_flux_fv=surface_flux)

solver = DGSEM(basis, surface_flux, volume_integral)

coordinates_min = (-1.0, -1.0)
coordinates_max = ( 1.0,  1.0)
mesh = TreeMesh(coordinates_min, coordinates_max,
                initial_refinement_level=2,
                n_cells_max=30_000)


semi = SemidiscretizationHyperbolic(mesh, equations, initial_condition, solver)


###############################################################################
# ODE solvers, callbacks etc.

tspan = (0.0, 2.0)
ode = semidiscretize(semi, tspan)

summary_callback = SummaryCallback()

analysis_interval = 100
analysis_callback = AnalysisCallback(semi, interval=analysis_interval)

alive_callback = AliveCallback(analysis_interval=analysis_interval)

save_solution = SaveSolutionCallback(interval=10000000,
                                     save_initial_solution=true,
                                     save_final_solution=true,
				     output_directory=joinpath(@__DIR__,"out"*string(mesh.tree.length)*"_n"*string(polydeg)),
                                     solution_variables=cons2prim)

stepsize_callback = StepsizeCallback(cfl=0.9)

callbacks = CallbackSet(summary_callback,
                        analysis_callback, alive_callback,
                        stepsize_callback,
			save_solution)


###############################################################################
# run the simulation

sol = Trixi.solve(ode, 
            dt=1.0, # solve needs some value here but it will be overwritten by the stepsize_callback
            save_everystep=false, callback=callbacks);
summary_callback() # print the timer summary

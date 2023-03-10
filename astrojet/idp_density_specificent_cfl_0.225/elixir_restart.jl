
using OrdinaryDiffEq
using Trixi

###############################################################################
# semidiscretization of the compressible Euler equations
gamma = 5/3
equations = CompressibleEulerEquations2D(gamma)

# Initial condition adopted from
# - Yong Liu, Jianfang Lu, and Chi-Wang Shu
#   An oscillation free discontinuous Galerkin method for hyperbolic systems
#   https://tinyurl.com/c76fjtx4
# Mach = 2000 jet
function initial_condition_astro_jet(x, t, equations::CompressibleEulerEquations2D)
  @unpack gamma = equations
  rho = 0.5
  v1 = 0
  v2 = 0
  p =  0.4127
  # add inflow for t>0 at x=-0.5
  # domain size is [-0.5,+0.5]^2
  if (x[1] ≈ -0.5) && (abs(x[2]) < 0.05)
    rho = 5
    v1 = 800 # about Mach number Ma = 2000
    v2 = 0
    p = 0.4127
  end
  return prim2cons(SVector(rho, v1, v2, p), equations)
end
initial_condition = initial_condition_astro_jet


restart_filename = joinpath("out", "restart_000001.h5")

boundary_conditions = (
                       x_neg=BoundaryConditionCharacteristic(initial_condition_astro_jet),
                       x_pos=BoundaryConditionCharacteristic(initial_condition_astro_jet),
                       y_neg=boundary_condition_periodic,
                       y_pos=boundary_condition_periodic,
                      )

surface_flux = flux_lax_friedrichs # HLLC needs more shock capturing (alpha_max)
volume_flux  = flux_ranocha # works with Chandrashekar flux as well
polydeg = 3
basis = LobattoLegendreBasis(polydeg)

# shock capturing necessary for this tough example
indicator_sc = IndicatorIDP(equations, basis;
		            IDPDensityTVD=true,
			    IDPSpecEntropy=true,
                            IDPPositivity=false,
                            IDPCheckBounds=true,
			    BarStates=true,
			    indicator_smooth=false)
volume_integral=VolumeIntegralShockCapturingSubcell(indicator_sc; volume_flux_dg=volume_flux,
                                                                  volume_flux_fv=surface_flux)
solver = DGSEM(basis, surface_flux, volume_integral)

coordinates_min = (-0.5, -0.5)
coordinates_max = ( 0.5,  0.5)

mesh = TreeMesh(coordinates_min, coordinates_max,
                initial_refinement_level=8,
                periodicity=(false,true),
                n_cells_max=100_000)
semi = SemidiscretizationHyperbolic(mesh, equations, initial_condition, solver, boundary_conditions=boundary_conditions)

###############################################################################
# ODE solvers, callbacks etc.

tspan = (0.0, 0.001)
ode = semidiscretize(semi, tspan)

summary_callback = SummaryCallback()

analysis_interval = 1000
analysis_callback = AnalysisCallback(semi, interval=analysis_interval)

alive_callback = AliveCallback(analysis_interval=analysis_interval)

# The SaveRestartCallback allows to save a file from which a Trixi simulation can be restarted

save_solution = SaveSolutionCallback(interval=200,
                                     save_initial_solution=true,
                                     save_final_solution=true,
				     output_directory=joinpath(@__DIR__,"out"*string(mesh.tree.length)),
                                     solution_variables=cons2prim)

stepsize_callback = StepsizeCallback(cfl=0.225)

callbacks = CallbackSet(summary_callback,
                        analysis_callback, 
			alive_callback,
                        stepsize_callback,
                        save_solution)

###############################################################################
# run the simulation
sol = Trixi.solve(ode,
                  dt=1.0, # solve needs some value here but it will be overwritten by the stepsize_callback
                  callback=callbacks, maxiters=100_000_000);
summary_callback() # print the timer summary

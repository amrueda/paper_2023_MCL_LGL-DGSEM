using OrdinaryDiffEq
using Trixi

trixi_include("mcl_positvity_density_pressure_sharp_cfl0.9_t6.7.jl")

restart_filename = "out/kelvinhelmholtz/mcl_positivity_density_pressure_t6_7/restart_3119274.h5"

tspan = (load_time(restart_filename), 10.0)
ode = semidiscretize(semi, tspan, restart_filename);

save_solution = SaveSolutionCallback(output_directory="out/kelvinhelmholtz/mcl_positivity_density_pressure_t10/",
                                     interval=100000,
                                     save_initial_solution=true,
                                     save_final_solution=true,
                                     solution_variables=cons2prim)

save_restart = SaveRestartCallback(output_directory="out/kelvinhelmholtz/mcl_positivity_density_pressure_t10/",
                                   interval=1000000,
                                   save_final_restart=true)

callbacks = CallbackSet(summary_callback,
                        stepsize_callback,
                        analysis_callback, alive_callback,
                        save_restart,
                        save_solution)

sol = Trixi.solve(ode,
                  maxiters=1e7, dt=1.0, # solve needs some value here but it will be overwritten by the stepsize_callback
                  callback=callbacks);
summary_callback() # print the timer summary

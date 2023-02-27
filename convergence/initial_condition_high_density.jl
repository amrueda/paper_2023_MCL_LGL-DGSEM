using Trixi

function initial_condition_density_wave_highdensity(x, t, equations::CompressibleEulerEquations2D)
  v1 = 0.1
  v2 = 0.2
  rho = 2.0 + 0.98 * sinpi(2 * (x[1] + x[2] - t * (v1 + v2)))
  rho_v1 = rho * v1
  rho_v2 = rho * v2
  p = 20
  rho_e = p / (equations.gamma - 1) + 1/2 * rho * (v1^2 + v2^2)
  return SVector(rho, rho_v1, rho_v2, rho_e)
end

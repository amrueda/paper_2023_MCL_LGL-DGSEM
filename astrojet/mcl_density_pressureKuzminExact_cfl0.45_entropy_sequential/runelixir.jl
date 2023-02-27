using Trixi
open(joinpath(@__DIR__,"log.txt"), "w") do io
     redirect_stdout(io) do
         trixi_include(joinpath(@__DIR__,"elixir.jl"))
     end
 end

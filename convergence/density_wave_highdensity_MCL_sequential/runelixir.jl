open(joinpath(@__DIR__,"log_n3.txt"), "w") do io
     redirect_stdout(io) do
         convergence_test(joinpath(@__DIR__,"elixir.jl"),4,polydeg=3)
     end
end
open(joinpath(@__DIR__,"log_n4.txt"), "w") do io
     redirect_stdout(io) do
         convergence_test(joinpath(@__DIR__,"elixir.jl"),4,polydeg=4)
     end
 end

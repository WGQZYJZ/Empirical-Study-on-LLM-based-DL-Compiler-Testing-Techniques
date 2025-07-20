input = torch.rand(5, 4)
input_sobol = torch.quasirandom.SobolEngine(4).draw(5)
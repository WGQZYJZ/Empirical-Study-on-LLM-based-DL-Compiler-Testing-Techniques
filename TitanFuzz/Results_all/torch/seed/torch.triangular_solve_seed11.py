A = torch.randn(3, 3)
b = torch.randn(3, 4)
x = torch.triangular_solve(b, A, upper=False)[0]
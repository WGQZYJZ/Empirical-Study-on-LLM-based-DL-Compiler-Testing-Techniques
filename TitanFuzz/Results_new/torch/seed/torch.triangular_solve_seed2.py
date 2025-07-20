A = torch.randn(3, 3)
b = torch.randn(3, 1)
x = torch.triangular_solve(b, A, upper=True)[0]
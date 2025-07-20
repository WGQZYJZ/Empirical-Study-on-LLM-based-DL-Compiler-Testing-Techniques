A = torch.randn(3, 3)
b = torch.randn(3, 1)
x = torch.cholesky_solve(b, A)
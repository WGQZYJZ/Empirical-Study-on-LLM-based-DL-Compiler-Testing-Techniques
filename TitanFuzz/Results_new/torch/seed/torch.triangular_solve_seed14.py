A = torch.randn(5, 5, requires_grad=True)
b = torch.randn(5, 5, requires_grad=True)
x = torch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)
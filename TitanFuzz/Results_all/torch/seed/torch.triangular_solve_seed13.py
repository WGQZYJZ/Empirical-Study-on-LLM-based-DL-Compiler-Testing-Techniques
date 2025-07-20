A = torch.rand(3, 3)
b = torch.rand(3, 1)
x = torch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)[0]
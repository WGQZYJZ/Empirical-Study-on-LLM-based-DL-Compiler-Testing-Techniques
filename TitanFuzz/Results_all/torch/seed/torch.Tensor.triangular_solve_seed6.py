a = torch.randn(3, 3)
b = torch.randn(3, 2)
torch.Tensor.triangular_solve(b, a, upper=True, transpose=False, unitriangular=False)
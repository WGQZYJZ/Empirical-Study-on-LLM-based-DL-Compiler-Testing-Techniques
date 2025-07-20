a = torch.randn(2, 3, 3)
b = torch.randn(2, 3, 3)
torch.Tensor.triangular_solve(a, b, upper=True, transpose=False, unitriangular=False)
input_tensor = torch.randn(3, 3)
A = torch.randn(3, 3)
torch.Tensor.triangular_solve(input_tensor, A, upper=True, transpose=False, unitriangular=False)
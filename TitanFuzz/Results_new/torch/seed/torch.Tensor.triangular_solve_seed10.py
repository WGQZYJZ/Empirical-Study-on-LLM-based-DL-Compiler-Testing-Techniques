input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float)
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float)
torch.Tensor.triangular_solve(input_tensor, A, upper=True, transpose=False, unitriangular=False)
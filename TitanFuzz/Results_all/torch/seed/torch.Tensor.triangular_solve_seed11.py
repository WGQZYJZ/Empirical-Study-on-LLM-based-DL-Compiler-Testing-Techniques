A_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
X_tensor = torch.Tensor.triangular_solve(_input_tensor, A_tensor, upper=True, transpose=False, unitriangular=False)
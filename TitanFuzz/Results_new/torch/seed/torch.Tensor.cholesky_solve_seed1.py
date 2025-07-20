input_tensor = torch.tensor([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [3.0, 4.0, 5.0]])
input2 = torch.tensor([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [3.0, 4.0, 5.0]])
output = torch.Tensor.cholesky_solve(input_tensor, input2, upper=False)
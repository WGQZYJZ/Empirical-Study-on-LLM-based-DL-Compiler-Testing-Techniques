input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.isclose(input_tensor, other)
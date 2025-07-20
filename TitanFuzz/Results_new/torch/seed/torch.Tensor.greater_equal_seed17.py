input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 1, 1], [2, 2, 2]])
result = torch.Tensor.greater_equal(input_tensor, other)
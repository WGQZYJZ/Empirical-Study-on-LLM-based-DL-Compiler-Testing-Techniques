input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 1, 1], [1, 1, 1]])
result = torch.Tensor.sub_(input_tensor, other)
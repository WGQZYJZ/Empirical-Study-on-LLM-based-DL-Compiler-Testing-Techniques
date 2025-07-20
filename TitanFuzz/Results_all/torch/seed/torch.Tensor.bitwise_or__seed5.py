input_tensor = torch.tensor([[1, 0], [0, 1]])
other = torch.tensor([[1, 1], [1, 0]])
result = torch.Tensor.bitwise_or_(input_tensor, other)
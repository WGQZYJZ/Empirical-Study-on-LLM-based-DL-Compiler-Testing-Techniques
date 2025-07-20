input_tensor = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
other = torch.tensor([[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 0]])
result = torch.Tensor.bitwise_and(input_tensor, other)
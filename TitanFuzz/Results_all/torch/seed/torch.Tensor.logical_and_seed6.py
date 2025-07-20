input_tensor = torch.Tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
other = torch.Tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
result = torch.Tensor.logical_and(input_tensor, other)
input_tensor = torch.tensor([[1, 0, 1, 0], [1, 1, 0, 0]], dtype=torch.bool)
other = torch.tensor([[1, 1, 0, 0], [1, 0, 1, 0]], dtype=torch.bool)
result = torch.Tensor.logical_and_(input_tensor, other)
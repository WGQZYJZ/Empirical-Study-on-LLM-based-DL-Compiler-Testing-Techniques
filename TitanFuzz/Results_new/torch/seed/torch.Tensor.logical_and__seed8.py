input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.bool)
other = torch.randint(0, 2, (3, 3), dtype=torch.bool)
result = torch.Tensor.logical_and_(input_tensor, other)
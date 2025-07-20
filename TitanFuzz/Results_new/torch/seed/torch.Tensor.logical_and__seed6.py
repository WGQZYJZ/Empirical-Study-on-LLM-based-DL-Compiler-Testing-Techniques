input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.bool)
other = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.bool)
torch.Tensor.logical_and_(input_tensor, other)
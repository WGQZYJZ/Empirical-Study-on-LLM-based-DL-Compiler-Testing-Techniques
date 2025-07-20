input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
other = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
torch.Tensor.logical_or_(input_tensor, other)
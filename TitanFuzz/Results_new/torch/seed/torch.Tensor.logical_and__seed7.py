input_tensor = torch.tensor([[1, 0, 1, 1], [1, 1, 0, 0]])
other = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0]])
torch.Tensor.logical_and_(input_tensor, other)
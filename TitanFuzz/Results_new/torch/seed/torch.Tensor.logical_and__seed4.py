input_tensor = torch.tensor([[True, True], [False, False]])
other = torch.tensor([[True, False], [True, False]])
torch.Tensor.logical_and_(input_tensor, other)
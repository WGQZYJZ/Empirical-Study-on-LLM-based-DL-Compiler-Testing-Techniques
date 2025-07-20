input_tensor = torch.tensor([[True, False, True], [False, True, False]], dtype=torch.bool)
other = torch.tensor([[True, True, False], [False, True, False]], dtype=torch.bool)
torch.Tensor.logical_and_(input_tensor, other)
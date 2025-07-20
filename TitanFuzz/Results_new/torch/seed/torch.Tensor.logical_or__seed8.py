input_tensor = torch.Tensor([[True, False], [True, True]])
other = torch.Tensor([[True, True], [False, False]])
result = torch.Tensor.logical_or_(input_tensor, other)
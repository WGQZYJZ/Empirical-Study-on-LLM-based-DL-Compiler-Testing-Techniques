input_tensor = torch.tensor([[True, False], [False, True]])
other = torch.tensor([[True, True], [False, True]])
output_tensor = torch.Tensor.logical_and_(input_tensor, other)
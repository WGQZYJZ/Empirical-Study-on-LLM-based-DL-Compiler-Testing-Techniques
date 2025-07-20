input_tensor = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
other = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
torch.Tensor.logical_xor_(input_tensor, other)
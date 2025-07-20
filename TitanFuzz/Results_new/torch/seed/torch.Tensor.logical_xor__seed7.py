input_tensor = torch.tensor([[True, False], [True, False]])
other = torch.tensor([[True, False], [True, True]])
torch.Tensor.logical_xor_(input_tensor, other)
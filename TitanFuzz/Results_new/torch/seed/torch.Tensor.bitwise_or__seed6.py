_input_tensor = torch.tensor([[True, False], [True, True]])
other = torch.tensor([[True, True], [True, False]])
torch.Tensor.bitwise_or_(_input_tensor, other)
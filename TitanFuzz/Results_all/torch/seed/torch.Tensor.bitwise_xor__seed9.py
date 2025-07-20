input_tensor = torch.tensor([[True, False], [False, True]])
other = torch.tensor([[True, True], [False, True]])
torch.Tensor.bitwise_xor_(input_tensor, other)
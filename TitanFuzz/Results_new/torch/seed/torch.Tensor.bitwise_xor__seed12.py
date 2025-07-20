input_tensor = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
other = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
output = torch.Tensor.bitwise_xor_(input_tensor, other)
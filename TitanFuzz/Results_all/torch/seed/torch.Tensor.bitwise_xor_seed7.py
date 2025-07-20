input_tensor = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
other = torch.tensor([[True, True], [False, False], [True, True], [False, False]])
output_tensor = torch.Tensor.bitwise_xor(input_tensor, other)
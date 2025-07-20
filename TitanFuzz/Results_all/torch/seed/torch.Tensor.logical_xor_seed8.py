input_tensor = torch.Tensor([[True, True], [True, False], [False, True], [False, False]])
other = torch.Tensor([[True, True], [True, False], [False, True], [False, False]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other)
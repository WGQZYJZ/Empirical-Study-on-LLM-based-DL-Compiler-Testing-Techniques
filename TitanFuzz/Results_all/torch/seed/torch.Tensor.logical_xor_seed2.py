input_tensor = torch.tensor([[True, False], [True, True]])
other = torch.tensor([[True, True], [False, True]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other)
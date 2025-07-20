input_tensor = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other=True)
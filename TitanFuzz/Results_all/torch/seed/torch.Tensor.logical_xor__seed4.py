_input_tensor = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
other = torch.tensor([[False, True], [True, False]], dtype=torch.bool)
_output_tensor = torch.Tensor.logical_xor_(_input_tensor, other)
_input_tensor = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
other = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
torch.Tensor.logical_xor_(_input_tensor, other)
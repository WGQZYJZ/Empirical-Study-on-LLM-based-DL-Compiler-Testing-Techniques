input_tensor = torch.tensor([[True, False, False], [False, True, False], [False, False, True]], dtype=torch.bool)
output_tensor = torch.Tensor.logical_not_(input_tensor)
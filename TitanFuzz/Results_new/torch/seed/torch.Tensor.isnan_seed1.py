_input_tensor = torch.randn(4, 4)
_input_tensor[(1, 1)] = float('nan')
_output_tensor = torch.Tensor.isnan(_input_tensor)
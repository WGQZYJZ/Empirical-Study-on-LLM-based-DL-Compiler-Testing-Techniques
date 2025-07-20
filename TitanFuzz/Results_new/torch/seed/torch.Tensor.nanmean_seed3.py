_input_tensor = torch.randn(100, 100, 100)
_input_tensor[(_input_tensor > 0.5)] = float('nan')
_output_tensor = torch.Tensor.nanmean(_input_tensor, dim=2)
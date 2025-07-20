_input_tensor = torch.randn(2, 3, 4)
_output_tensor = torch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)
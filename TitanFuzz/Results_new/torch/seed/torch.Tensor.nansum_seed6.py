_input_tensor = torch.randn(2, 3)
_output = torch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)
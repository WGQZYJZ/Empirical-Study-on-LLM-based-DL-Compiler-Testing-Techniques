_input_tensor = torch.randn(3, 3, requires_grad=True)
_output_tensor = torch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)
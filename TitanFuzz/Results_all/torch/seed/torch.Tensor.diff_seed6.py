_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.diff(_input_tensor, n=1, dim=(- 1), prepend=None, append=None)
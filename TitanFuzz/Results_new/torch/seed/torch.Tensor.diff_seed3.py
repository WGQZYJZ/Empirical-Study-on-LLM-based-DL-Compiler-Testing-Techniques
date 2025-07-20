input_tensor = torch.randn(5, 2)
output_tensor = torch.Tensor.diff(input_tensor, n=1, dim=(- 1), prepend=None, append=None)
input_tensor = torch.randn(2, 3, 4, 5)
other = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.arctanh_(input_tensor, other)
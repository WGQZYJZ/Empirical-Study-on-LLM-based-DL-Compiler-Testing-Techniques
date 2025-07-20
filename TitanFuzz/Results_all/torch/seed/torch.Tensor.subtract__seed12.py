input_tensor = torch.randn(3, 2)
other = torch.randn(3, 2)
output_tensor = torch.Tensor.subtract_(input_tensor, other)
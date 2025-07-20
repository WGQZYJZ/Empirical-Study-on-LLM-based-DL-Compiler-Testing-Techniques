input_tensor = torch.randn(3, 4)
other = torch.ones(3, 4)
output_tensor = torch.Tensor.subtract_(input_tensor, other)
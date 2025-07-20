input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
output_tensor = torch.Tensor.copysign_(input_tensor, other)
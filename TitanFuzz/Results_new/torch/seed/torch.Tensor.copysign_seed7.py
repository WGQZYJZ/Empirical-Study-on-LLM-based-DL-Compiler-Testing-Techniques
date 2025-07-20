input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
output_tensor = torch.Tensor.copysign(input_tensor, other)
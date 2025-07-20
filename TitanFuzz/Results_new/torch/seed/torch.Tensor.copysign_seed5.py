input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
output = torch.Tensor.copysign(input_tensor, other)
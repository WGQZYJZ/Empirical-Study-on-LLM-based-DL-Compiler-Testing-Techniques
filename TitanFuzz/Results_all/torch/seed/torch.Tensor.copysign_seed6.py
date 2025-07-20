input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
output_tensor = torch.Tensor.copysign(input_tensor, other)
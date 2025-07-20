input_tensor = torch.randn(4, 4)
other_tensor = torch.randn(4, 4)
output_tensor = torch.copysign(input_tensor, other_tensor)
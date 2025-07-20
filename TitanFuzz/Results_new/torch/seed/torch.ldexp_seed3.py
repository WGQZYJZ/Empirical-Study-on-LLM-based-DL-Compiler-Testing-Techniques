input_tensor = torch.rand(3, 3)
other_tensor = torch.rand(3, 3)
output_tensor = torch.ldexp(input_tensor, other_tensor)
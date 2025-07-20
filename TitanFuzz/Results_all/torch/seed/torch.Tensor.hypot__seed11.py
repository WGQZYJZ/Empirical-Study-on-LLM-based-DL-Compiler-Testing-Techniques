_input_tensor = torch.rand(3, 5)
other = torch.rand(3, 5)
output_tensor = torch.Tensor.hypot_(_input_tensor, other)
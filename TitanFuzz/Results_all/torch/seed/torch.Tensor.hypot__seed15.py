input_tensor = torch.rand(3, 4)
other = torch.rand(3, 4)
output_tensor = torch.Tensor.hypot_(input_tensor, other)
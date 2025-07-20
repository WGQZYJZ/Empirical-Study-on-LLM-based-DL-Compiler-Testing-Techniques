input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
output_tensor = torch.Tensor.minimum(input_tensor, other)
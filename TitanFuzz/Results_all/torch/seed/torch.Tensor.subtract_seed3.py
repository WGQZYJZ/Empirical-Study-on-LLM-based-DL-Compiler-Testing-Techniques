input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
output_tensor = torch.Tensor.subtract(input_tensor, other)
output_tensor = input_tensor.subtract(other)
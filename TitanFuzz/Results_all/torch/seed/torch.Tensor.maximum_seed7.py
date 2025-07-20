input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
output_tensor = torch.Tensor.maximum(input_tensor, other)
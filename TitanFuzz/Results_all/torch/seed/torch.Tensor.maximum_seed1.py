input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
result = torch.Tensor.maximum(input_tensor, other)
input_tensor = torch.randn(3, 5)
other = torch.randn(3, 5)
result = torch.Tensor.xlogy(input_tensor, other)
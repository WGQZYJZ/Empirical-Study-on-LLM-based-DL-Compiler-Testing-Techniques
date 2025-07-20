input_tensor = torch.randn(1, 3)
other = torch.randn(1, 3)
result = torch.Tensor.xlogy(input_tensor, other)
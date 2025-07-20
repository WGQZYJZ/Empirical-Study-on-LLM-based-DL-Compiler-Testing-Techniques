input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
result = torch.Tensor.xlogy_(input_tensor, other)
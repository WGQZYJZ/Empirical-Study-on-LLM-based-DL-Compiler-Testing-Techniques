input_tensor = torch.randn(5, 3)
other = torch.randn(5, 3)
result = torch.Tensor.subtract_(input_tensor, other)
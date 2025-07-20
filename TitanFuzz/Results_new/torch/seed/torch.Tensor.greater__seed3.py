input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
result = torch.Tensor.greater_(input_tensor, other)
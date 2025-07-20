input_tensor = torch.randn(100)
histogram = torch.Tensor.histogram(input_tensor, bins=10)
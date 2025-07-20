input = torch.randn(100)
hist = torch.Tensor.histogram(input, bins=10)
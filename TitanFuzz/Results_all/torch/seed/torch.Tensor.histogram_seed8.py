input = torch.randn(100)
bins = 10
hist = torch.Tensor.histogram(input, bins)
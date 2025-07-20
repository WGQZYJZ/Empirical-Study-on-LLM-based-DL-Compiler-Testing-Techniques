input = torch.randn(1, 1, 4)
max_pooling = torch.nn.AdaptiveMaxPool1d(1)
output = max_pooling(Variable(input))
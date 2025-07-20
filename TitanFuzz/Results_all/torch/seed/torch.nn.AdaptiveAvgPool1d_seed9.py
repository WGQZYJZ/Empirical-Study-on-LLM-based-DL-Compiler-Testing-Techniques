input = torch.randn(1, 1, 4)
avg_pool = torch.nn.AdaptiveAvgPool1d(1)
output = avg_pool(Variable(input))
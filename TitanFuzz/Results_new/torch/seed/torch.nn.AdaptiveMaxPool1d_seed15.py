input = Variable(torch.randn(1, 1, 4))
pool = torch.nn.AdaptiveMaxPool1d(1)
output = pool(input)
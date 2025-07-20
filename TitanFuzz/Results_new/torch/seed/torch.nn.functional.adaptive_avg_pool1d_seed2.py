input = Variable(torch.randn(1, 1, 10))
output = torch.nn.functional.adaptive_avg_pool1d(input, 1)
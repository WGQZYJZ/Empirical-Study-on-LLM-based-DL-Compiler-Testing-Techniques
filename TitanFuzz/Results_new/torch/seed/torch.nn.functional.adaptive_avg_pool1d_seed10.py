input = Variable(torch.randn(1, 64, 8))
output = torch.nn.functional.adaptive_avg_pool1d(input, (1,))
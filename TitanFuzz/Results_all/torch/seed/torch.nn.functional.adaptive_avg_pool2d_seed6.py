input = Variable(torch.randn(1, 3, 6, 6))
output = torch.nn.functional.adaptive_avg_pool2d(input, (2, 2))
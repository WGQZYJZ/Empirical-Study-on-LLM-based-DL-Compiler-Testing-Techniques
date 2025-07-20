input = Variable(torch.randn(1, 1, 6, 6))
output = torch.nn.functional.adaptive_max_pool2d(input, (3, 3))
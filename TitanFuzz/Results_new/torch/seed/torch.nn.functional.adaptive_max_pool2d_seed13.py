input = Variable(torch.randn(1, 1, 28, 28))
output = torch.nn.functional.adaptive_max_pool2d(input, (1, 1))
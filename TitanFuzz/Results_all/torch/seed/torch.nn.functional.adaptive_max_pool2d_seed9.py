input = Variable(torch.randn(1, 1, 5, 5))
torch.nn.functional.adaptive_max_pool2d(input, (2, 2))
torch.nn.functional.adaptive_max_pool2d(input, (3, 2))
input = Variable(torch.randn(1, 64, 8, 8, 8))
output = torch.nn.functional.adaptive_max_pool3d(input, (1, 1, 1))
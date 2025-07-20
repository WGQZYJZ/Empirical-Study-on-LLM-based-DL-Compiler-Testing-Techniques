input = Variable(torch.randn(1, 1, 6, 6))
output = torch.nn.functional.adaptive_max_pool2d(input, (2, 2))
output = torch.nn.functional.adaptive_max_pool2d(input, (2, 2), return_indices=True)
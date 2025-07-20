input = Variable(torch.randn(1, 1, 4, 4))
output = torch.nn.functional.max_pool2d(input, 2)
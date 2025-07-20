input = Variable(torch.randn(1, 1, 5, 5))
weight = Variable(torch.randn(1, 1, 3, 3))
conv2d = torch.nn.functional.conv2d(input, weight)
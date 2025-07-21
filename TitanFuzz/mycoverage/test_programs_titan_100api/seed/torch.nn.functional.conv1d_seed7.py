input = Variable(torch.randn(1, 1, 10))
weight = Variable(torch.randn(1, 1, 3))
bias = Variable(torch.randn(1))
output = torch.nn.functional.conv1d(input, weight, bias)
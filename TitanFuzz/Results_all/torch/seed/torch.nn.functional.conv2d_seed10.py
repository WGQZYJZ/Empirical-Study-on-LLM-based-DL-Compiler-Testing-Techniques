input = Variable(torch.randn(1, 1, 5, 5))
weight = Variable(torch.randn(1, 1, 3, 3))
output = torch.nn.functional.conv2d(input, weight, stride=1, padding=0)
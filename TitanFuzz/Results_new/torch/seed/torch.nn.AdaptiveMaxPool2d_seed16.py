input = Variable(torch.randn(1, 1, 4, 4))
output = torch.nn.AdaptiveMaxPool2d(3)(input)
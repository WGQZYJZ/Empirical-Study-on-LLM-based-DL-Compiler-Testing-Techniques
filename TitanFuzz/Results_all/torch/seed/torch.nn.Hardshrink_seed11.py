input = Variable(torch.randn(1, 3, 5, 5))
hardshrink = torch.nn.Hardshrink(lambd=0.5)
output = hardshrink(input)
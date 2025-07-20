input_data = Variable(torch.randn(1, 3, 3))
hardshrink = torch.nn.Hardshrink(lambd=0.5)
output = hardshrink(input_data)
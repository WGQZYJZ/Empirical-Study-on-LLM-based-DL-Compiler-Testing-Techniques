x = Variable(torch.randn(1, 1, 3, 3))
y = torch.nn.functional.hardsigmoid(x)
x = Variable(torch.Tensor([(- 2), (- 1), 0, 1, 2]))
hardshrink = torch.nn.Hardshrink(lambd=0.5)
y = hardshrink(x)
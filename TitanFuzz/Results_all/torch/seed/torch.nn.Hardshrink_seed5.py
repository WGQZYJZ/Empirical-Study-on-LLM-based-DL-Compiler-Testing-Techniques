x = torch.randn(3, 3)
hardshrink = torch.nn.Hardshrink(lambd=0.5)
y = hardshrink(x)
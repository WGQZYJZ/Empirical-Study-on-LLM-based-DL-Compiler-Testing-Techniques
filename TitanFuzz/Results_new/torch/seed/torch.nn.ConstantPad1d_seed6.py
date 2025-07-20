x = torch.randn(2, 3, 3)
padding = (0, 1)
value = 1
y = torch.nn.ConstantPad1d(padding, value)(x)
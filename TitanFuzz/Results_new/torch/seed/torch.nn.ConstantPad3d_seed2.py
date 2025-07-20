input = torch.randn(1, 1, 2, 2, 2)
padding = (1, 1, 1, 1, 1, 1)
value = 0
output = torch.nn.ConstantPad3d(padding, value)(input)
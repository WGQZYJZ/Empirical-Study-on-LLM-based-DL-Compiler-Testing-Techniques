input_data = torch.randn(1, 1, 3, 3, 3)
padding = (1, 1, 1, 1, 1, 1)
value = 0
output = torch.nn.ConstantPad3d(padding, value)(input_data)
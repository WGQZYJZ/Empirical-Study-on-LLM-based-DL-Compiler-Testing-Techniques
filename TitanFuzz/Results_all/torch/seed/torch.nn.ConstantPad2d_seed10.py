input = torch.randn(1, 3, 3, 3)
padding = (1, 1, 1, 1)
value = 0
output = torch.nn.ConstantPad2d(padding, value)(input)
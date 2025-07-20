input = torch.ones(1, 1, 3, 3)
pad = torch.nn.ConstantPad2d(padding=1, value=0)
output = pad(input)
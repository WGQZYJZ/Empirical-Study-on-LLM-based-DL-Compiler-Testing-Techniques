input = torch.randn(1, 3, 3, 3)
pad = torch.nn.ConstantPad2d((1, 1, 1, 1), 0)
output = pad(input)
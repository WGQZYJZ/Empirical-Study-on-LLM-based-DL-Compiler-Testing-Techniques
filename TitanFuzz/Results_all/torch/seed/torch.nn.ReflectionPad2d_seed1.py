input = torch.randn(1, 1, 3, 3)
pad = torch.nn.ReflectionPad2d(padding=1)
output = pad(input)
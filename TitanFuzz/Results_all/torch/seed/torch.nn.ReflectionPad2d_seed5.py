input_data = torch.randn(1, 1, 3, 3)
pad = torch.nn.ReflectionPad2d((1, 1, 1, 1))
output = pad(input_data)
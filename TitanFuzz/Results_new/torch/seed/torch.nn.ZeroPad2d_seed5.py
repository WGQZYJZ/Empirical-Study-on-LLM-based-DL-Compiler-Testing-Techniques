input = torch.randn(1, 1, 4, 4)
padding = (1, 2, 3, 4)
output = torch.nn.ZeroPad2d(padding)(input)
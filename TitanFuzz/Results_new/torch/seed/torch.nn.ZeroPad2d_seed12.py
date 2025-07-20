input_tensor = torch.randn(1, 1, 4, 4)
padding = (1, 1, 1, 1)
zero_pad = torch.nn.ZeroPad2d(padding)
output_tensor = zero_pad(input_tensor)
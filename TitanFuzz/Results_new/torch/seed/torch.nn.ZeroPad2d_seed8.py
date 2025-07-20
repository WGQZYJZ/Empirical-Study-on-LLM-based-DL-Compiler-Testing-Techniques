input = torch.tensor([[[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]], dtype=torch.float32)
padding = (2, 2, 2, 2)
zero_pad = torch.nn.ZeroPad2d(padding)
output = zero_pad(input)
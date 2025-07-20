input = torch.tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]])
padding = (1, 1, 2, 2)
value = 0
output = torch.nn.ConstantPad2d(padding, value)(input)
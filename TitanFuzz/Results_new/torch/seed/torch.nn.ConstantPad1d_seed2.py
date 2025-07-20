input = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])
padding = (5, 5)
value = 0
output = torch.nn.ConstantPad1d(padding, value)(input)
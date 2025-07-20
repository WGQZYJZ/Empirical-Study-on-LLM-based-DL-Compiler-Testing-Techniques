input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=torch.float)
padding = (1, 2)
value = 0
result = torch.nn.ConstantPad1d(padding, value)(input)
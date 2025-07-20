input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
padding = (1, 2)
value = 0
output = torch.nn.ConstantPad1d(padding, value)(input)
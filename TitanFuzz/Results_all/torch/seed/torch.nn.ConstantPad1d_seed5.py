input = torch.arange(1, 9, dtype=torch.float32).view(1, 2, 4).repeat(1, 1, 1)
output = torch.nn.ConstantPad1d((1, 2), 0)(input)
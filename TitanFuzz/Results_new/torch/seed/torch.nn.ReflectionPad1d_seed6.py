input = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]], dtype=torch.float)
pad = torch.nn.ReflectionPad1d(2)
output = pad(input)
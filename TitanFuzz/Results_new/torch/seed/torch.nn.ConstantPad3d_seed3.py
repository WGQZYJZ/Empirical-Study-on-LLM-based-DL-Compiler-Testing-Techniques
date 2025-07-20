input_data = torch.randint(1, 5, (2, 3, 4, 5), dtype=torch.float32)
pad_size = (1, 2, 3, 4)
value = 0.0
pad3d = torch.nn.ConstantPad3d(pad_size, value)
output = pad3d(input_data)
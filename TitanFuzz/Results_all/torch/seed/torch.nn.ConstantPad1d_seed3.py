input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
pad_size = 1
value = 0
padded_input = torch.nn.ConstantPad1d(pad_size, value)(input)
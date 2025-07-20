input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
pad1d = torch.nn.ConstantPad1d((1, 1), 0)
output = pad1d(input_data)
input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]], dtype=torch.float32)
padding = (1, 1, 1, 1)
value = 0
pad = torch.nn.ConstantPad2d(padding, value)
output_data = pad(input_data)
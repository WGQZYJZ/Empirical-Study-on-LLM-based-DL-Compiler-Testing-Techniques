input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
output = torch.nn.ConstantPad2d((1, 2, 3, 4), 0)(input_data)
input_data = torch.tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]])
padding = (1, 1, 1, 1, 1, 1)
value = 0
output_data = torch.nn.ConstantPad3d(padding, value)(input_data)
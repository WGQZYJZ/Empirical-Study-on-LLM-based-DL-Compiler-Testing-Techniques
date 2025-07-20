input_data = torch.randn(1, 1, 3, 3, 3)
padding_value = 0
padding = (1, 1, 1, 1, 1, 1)
output_data = torch.nn.ConstantPad3d(padding, padding_value)(input_data)
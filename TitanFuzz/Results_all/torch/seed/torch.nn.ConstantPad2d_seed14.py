input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
padding = torch.nn.ConstantPad2d((1, 1, 1, 1), 0)
output = padding(input_data)
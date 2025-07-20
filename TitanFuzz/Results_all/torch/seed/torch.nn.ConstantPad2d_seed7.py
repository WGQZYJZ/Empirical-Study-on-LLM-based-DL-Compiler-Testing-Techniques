input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=torch.float32)
input = input.reshape(1, 3, 4)
padding = (0, 1, 0, 2)
value = 0
output = torch.nn.ConstantPad2d(padding, value)(input)
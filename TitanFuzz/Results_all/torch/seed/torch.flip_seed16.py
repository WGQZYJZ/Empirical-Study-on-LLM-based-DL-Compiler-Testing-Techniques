input = torch.rand(2, 3, 5)
output = torch.flip(input, [0, 1])
output = torch.flip(input, [1])
output = torch.flip(input, [0])
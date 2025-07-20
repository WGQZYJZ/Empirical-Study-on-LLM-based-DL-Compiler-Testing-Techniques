input = torch.arange(1, 11)
output = torch.as_strided(input, (4, 2), (2, 1))
input[2] = 100
output[(0, 0)] = 100
output[(0, 0)] = 100
output[(0, 0)] = 100
input = torch.tensor([1, 2, 3])
output = torch.tile(input, (3, 1))
output = torch.tile(input, (1, 3))
input = torch.arange(1, 11)
input = input.view(1, 10)
output = torch.tile(input, (3, 1))
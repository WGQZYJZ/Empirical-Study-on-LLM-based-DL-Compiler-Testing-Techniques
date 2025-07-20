input = torch.tensor([(- 1), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
other = torch.tensor([(- 1), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
output = torch.special.zeta(input, other)
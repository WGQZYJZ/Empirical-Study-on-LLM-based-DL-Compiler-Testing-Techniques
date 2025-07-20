input = torch.randint(low=0, high=10, size=(3, 3))
other = torch.randint(low=0, high=10, size=(3, 3))
output = torch.bitwise_right_shift(input, other)
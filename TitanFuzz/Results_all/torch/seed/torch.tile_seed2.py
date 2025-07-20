x = torch.FloatTensor([[1, 2], [3, 4]])
y = torch.tile(x, (1, 2))
y = torch.tile(x, (2, 1))
y = torch.tile(x, (2, 2))
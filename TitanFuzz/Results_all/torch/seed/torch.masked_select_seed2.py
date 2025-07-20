input = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 1, 0], [0, 1, 0, 0]])
output = torch.masked_select(input, mask)
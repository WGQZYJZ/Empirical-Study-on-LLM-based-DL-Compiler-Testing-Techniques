x = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 1]])
y = torch.masked_select(x, mask)
z = torch.masked_select(x, mask, out=torch.empty(2, dtype=torch.float))
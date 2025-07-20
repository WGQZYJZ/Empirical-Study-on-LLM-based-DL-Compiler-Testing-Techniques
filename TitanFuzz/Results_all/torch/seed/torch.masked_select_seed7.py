x = torch.randn(3, 4)
mask = x.ge(0.5)
y = torch.masked_select(x, mask)
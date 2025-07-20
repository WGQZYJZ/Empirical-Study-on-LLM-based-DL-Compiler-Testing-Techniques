x = torch.randn(2, 3)
y = torch.masked_select(x, (x > 0))
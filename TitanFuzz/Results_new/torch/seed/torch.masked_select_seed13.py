a = torch.randn(2, 3)
b = torch.masked_select(a, (a > 0))
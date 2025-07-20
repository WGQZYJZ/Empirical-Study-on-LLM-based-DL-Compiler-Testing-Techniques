input = torch.randn(2, 3, 4)
mask = input.ge(0.5)
result = torch.masked_select(input, mask)
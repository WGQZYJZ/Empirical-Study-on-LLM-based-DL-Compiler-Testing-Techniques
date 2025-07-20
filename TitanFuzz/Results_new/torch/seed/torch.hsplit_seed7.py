input = torch.randn(8, 3)
output = torch.hsplit(input, 3)
output = torch.hsplit(input, [3, 5])
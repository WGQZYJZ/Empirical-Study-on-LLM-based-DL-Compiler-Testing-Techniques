input = torch.randn(2, 3, 5)
output = torch.movedim(input, 0, 1)
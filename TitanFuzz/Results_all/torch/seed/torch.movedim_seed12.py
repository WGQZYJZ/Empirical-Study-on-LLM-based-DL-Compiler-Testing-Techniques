input = torch.randn(2, 3, 4)
output = torch.movedim(input, 0, 1)
input = torch.randn(3, 4, 5)
output = torch.movedim(input, 0, 2)
input = torch.randn(2, 3, 4, 5)
output = torch.movedim(input, 0, (- 1))
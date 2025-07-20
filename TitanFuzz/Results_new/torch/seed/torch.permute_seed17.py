input = torch.randn(2, 3, 5)
output = torch.permute(input, (1, 0, 2))
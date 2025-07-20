input = torch.randn(1, 2, 3)
output = torch.permute(input, (1, 0, 2))
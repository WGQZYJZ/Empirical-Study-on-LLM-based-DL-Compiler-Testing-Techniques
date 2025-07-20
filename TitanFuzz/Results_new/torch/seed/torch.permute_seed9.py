input = torch.arange(0, 6).view(2, 3)
output = torch.permute(input, (1, 0))
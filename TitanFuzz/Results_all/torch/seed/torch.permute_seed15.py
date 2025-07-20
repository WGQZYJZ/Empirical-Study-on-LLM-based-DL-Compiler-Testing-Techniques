input = torch.arange(1, 13).view(3, 4)
output = torch.permute(input, (1, 0))
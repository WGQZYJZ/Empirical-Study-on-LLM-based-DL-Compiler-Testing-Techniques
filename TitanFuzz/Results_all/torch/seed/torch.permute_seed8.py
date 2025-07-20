input = torch.arange(0, 12).view(3, 4)
output = torch.permute(input, (1, 0))
output = torch.t(input)
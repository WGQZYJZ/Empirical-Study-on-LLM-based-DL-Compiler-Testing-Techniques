input = torch.randn(3, 5)
output = torch.mode(input, dim=0)
output = torch.mode(input, dim=1)
output = torch.mode(input, dim=(- 1))
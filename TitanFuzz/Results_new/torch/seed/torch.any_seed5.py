input = torch.randn(3, 4)
output = torch.any(input, dim=0)
output = torch.any(input, dim=1)
input = torch.randn(2, 3, 4)
output = torch.nansum(input, dim=2, keepdim=True)
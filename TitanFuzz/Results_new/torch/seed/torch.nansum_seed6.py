input = torch.randn(3, 4)
result = torch.nansum(input, dim=1, keepdim=True)
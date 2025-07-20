input = torch.randn(3, 4)
output = torch.median(input, dim=(- 1), keepdim=False, out=None)
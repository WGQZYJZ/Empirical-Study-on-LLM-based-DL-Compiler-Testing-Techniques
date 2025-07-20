input = torch.randn(3, 3)
input[(0, 0)] = float('nan')
input[(2, 2)] = float('nan')
output = torch.nanmedian(input, dim=(- 1), keepdim=False)
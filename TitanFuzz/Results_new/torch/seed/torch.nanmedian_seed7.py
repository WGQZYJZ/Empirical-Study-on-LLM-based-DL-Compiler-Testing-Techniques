input = torch.randn(3, 4)
input[(1, 2)] = float('nan')
input[(2, 3)] = float('nan')
output = torch.nanmedian(input, dim=(- 1), keepdim=False, out=None)
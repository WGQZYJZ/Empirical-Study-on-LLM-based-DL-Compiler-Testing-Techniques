input = torch.randn(3, 4)
input[1][1] = np.nan
result = torch.nanmedian(input)
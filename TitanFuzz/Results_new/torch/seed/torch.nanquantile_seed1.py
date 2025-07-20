input = torch.rand(100, 100)
input[0, :] = float('nan')
quantile = torch.nanquantile(input, q=0.5, dim=0, keepdim=False)
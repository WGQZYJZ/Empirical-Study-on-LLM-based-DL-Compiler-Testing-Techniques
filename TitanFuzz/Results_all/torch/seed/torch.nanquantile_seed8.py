input_data = torch.rand(5, 5)
quantile = torch.nanquantile(input_data, 0.5, dim=None, keepdim=False, out=None)
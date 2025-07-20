data = torch.rand(1000)
histc = torch.histc(data, bins=100, min=0, max=1)
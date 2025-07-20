x = torch.tensor([1, float('nan'), float('inf')])
y = torch.isnan(x)
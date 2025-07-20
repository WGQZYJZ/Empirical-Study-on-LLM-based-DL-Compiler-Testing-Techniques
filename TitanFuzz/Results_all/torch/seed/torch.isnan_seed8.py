x = torch.tensor([1, 2, float('nan'), float('inf'), float('-inf')])
y = torch.isnan(x)
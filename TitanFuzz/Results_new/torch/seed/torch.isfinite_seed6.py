x = torch.tensor([1, 2, float('inf'), float('nan')])
y = torch.isfinite(x)
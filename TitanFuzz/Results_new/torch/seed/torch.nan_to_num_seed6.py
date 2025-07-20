x = torch.tensor([[1, 2, 3], [4, 5, 6], [float('nan'), 7, 8]], dtype=torch.float)
y = torch.nan_to_num(x)
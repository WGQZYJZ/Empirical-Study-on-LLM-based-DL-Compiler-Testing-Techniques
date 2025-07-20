a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
b = torch.nanmean(a, dim=0)
b = torch.nanmean(a, dim=1)
b = torch.nanmean(a, dim=None)
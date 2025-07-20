input = torch.rand(3, 3, 3)
output = torch.nanmean(input, dim=2, keepdim=True)
input = torch.tensor([[1, torch.nan, 3], [4, 5, torch.nan]])
output = torch.nan_to_num(input)
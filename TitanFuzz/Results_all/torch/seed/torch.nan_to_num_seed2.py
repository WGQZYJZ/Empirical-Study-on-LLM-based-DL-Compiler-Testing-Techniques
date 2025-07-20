input = torch.tensor([[float('nan'), float('inf'), float('-inf')], [1, 2, 3], [0, 0, 0]])
output = torch.nan_to_num(input, 0.0, None, None)
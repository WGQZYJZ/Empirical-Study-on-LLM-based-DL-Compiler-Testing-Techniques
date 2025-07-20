input = torch.tensor([[float('nan'), float('inf'), float('-inf'), 0.0], [1.0, 2.0, 3.0, 4.0]])
output = torch.nan_to_num(input, nan=0.0, posinf=None, neginf=None)
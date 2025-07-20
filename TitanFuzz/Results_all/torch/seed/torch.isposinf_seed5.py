input = torch.tensor([float('inf'), float('-inf'), float('nan'), float('-nan')])
output = torch.isposinf(input)
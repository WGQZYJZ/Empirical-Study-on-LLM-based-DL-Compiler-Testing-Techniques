input_data = torch.tensor([(- float('inf')), float('inf'), float('nan'), float('-inf')])
result = torch.isneginf(input_data)
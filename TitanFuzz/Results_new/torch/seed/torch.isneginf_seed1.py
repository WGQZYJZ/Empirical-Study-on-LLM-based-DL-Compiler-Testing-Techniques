input = torch.tensor([(- float('inf')), float('-inf'), float('inf'), float('inf'), float('nan')])
result = torch.isneginf(input)
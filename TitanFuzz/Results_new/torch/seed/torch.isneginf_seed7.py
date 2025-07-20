input = torch.tensor([(- float('inf')), (- 1.0), 0.0, 1.0, float('inf'), float('nan')])
output = torch.isneginf(input)
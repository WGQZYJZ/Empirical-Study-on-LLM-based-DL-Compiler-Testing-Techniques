input = torch.tensor([(- float('inf')), float('inf'), float('nan')])
result = torch.isposinf(input)
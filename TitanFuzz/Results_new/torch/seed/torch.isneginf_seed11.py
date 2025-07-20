input = torch.tensor([(- float('inf')), (- 1), 0, 1, float('inf')])
output = torch.isneginf(input)
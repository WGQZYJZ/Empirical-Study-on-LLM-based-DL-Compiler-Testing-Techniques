input = torch.tensor([0.0, (- float('inf')), float('inf')])
output = torch.isneginf(input)
input_data = torch.tensor([(- float('inf')), float('-inf'), float('inf'), float('inf')])
output = torch.isneginf(input_data)
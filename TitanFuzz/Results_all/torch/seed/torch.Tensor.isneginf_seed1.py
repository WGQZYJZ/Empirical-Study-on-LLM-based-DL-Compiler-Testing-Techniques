input_tensor = torch.tensor([(- float('inf')), float('inf'), float('nan'), float('-inf'), float('inf'), float('nan')])
is_neginf = torch.Tensor.isneginf(input_tensor)
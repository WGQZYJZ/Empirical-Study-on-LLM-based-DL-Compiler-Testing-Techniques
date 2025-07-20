row = 3
col = 3
result = torch.triu_indices(row, col, offset=0, dtype=torch.long, device='cpu', layout=torch.strided)
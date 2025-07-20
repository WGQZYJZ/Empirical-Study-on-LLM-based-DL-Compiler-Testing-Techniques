row = 5
col = 5
offset = 0
result = torch.triu_indices(row, col, offset, dtype=torch.long, device='cpu', layout=torch.strided)
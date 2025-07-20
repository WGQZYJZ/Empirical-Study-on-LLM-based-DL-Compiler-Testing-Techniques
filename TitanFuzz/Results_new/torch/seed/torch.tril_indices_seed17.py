row = 4
col = 4
offset = (- 1)
data = torch.randn(row, col)
result = torch.tril_indices(row, col, offset, dtype=torch.long, device='cpu', layout=torch.strided)
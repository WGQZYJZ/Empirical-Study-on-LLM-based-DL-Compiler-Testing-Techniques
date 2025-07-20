row = torch.tensor(4)
col = torch.tensor(4)
torch.tril_indices(row, col, offset=0, dtype=torch.long, device='cpu', layout=torch.strided)
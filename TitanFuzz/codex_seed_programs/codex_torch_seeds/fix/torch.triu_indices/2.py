"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu_indices\ntorch.triu_indices(row, col, offset=0, *, dtype=torch.long, device='cpu', layout=torch.strided)\n"
import torch
input_data = torch.randn(4, 4)
print('Input data:\n', input_data)
indices = torch.triu_indices(4, 4, 0)
print('Indices:\n', indices)
output = torch.triu(input_data, 0)
print('Output:\n', output)
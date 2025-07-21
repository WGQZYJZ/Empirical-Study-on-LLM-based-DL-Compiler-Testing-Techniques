"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu_indices\ntorch.triu_indices(row, col, offset=0, *, dtype=torch.long, device='cpu', layout=torch.strided)\n"
import torch
input_data = torch.randn(3, 3)
print('Input data: ', input_data)
print('\nTriu indices: ', torch.triu_indices(3, 3))
print('\nTriu indices with offset 1: ', torch.triu_indices(3, 3, 1))
print('\nTriu indices with offset -1: ', torch.triu_indices(3, 3, (- 1)))
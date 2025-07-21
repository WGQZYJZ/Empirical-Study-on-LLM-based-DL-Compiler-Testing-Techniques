'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.corrcoef\ntorch.corrcoef(input)\n'
import torch
input_data = torch.rand(3, 3)
corr_matrix = torch.corrcoef(input_data)
print('Input data:')
print(input_data)
print('Correlation matrix:')
print(corr_matrix)
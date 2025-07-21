'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.det\ntorch.det(input)\n'
import torch
x = torch.Tensor([[1, 2], [3, 4]])
print('Input data: ')
print(x)
print('\nDeterminant: ')
print(torch.det(x))
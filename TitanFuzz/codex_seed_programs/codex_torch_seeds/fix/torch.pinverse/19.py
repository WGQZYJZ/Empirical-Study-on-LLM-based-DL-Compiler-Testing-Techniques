'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input = torch.randn(3, 5, dtype=torch.float64)
print('Input data: ', input)
print('Input data shape: ', input.shape)
pinverse = torch.pinverse(input)
print('Pseudo inverse: ', pinverse)
print('Pseudo inverse shape: ', pinverse.shape)
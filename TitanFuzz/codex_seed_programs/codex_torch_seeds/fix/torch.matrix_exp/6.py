'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_exp\ntorch.matrix_exp(input)\n'
import torch
x = torch.randn(2, 2)
print('Input: ', x)
output = torch.matrix_exp(x)
print('Output: ', output)
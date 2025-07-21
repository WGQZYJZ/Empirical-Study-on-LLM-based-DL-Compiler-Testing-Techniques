'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
data = torch.ones(2, 3, 4)
print('Input data: ', data)
result = torch.ravel(data)
print('Result: ', result)
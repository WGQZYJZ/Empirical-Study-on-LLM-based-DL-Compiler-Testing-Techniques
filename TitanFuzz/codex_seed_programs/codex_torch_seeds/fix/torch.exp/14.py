'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp\ntorch.exp(input, *, out=None)\n'
import torch
data = torch.randn(5, 3)
print('Input data: ', data)
output = torch.exp(data)
print('Output: ', output)
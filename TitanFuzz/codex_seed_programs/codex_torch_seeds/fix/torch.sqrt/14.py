'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
x = torch.rand(100)
print('Input:', x)
y = torch.sqrt(x)
print('Output:', y)
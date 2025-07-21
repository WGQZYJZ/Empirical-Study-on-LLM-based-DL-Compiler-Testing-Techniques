'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
x = torch.tensor([1, 2, 3, float('inf'), float('-inf'), float('nan')])
print('Input:', x)
print('torch.isinf(input)', torch.isinf(x))
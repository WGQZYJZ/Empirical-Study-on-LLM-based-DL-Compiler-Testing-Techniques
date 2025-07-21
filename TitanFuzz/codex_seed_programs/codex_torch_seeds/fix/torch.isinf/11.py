'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input = torch.randn(4, 4)
print('Input:', input)
print('Is Input Infinite:', torch.isinf(input))
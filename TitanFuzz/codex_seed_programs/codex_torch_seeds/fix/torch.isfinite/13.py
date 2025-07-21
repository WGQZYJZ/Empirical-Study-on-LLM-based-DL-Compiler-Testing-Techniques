'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
result = torch.isfinite(input)
print('Result: ', result)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input = torch.randn(2, 2)
print('Input: ', input)
output = torch.isinf(input)
print('Output: ', output)
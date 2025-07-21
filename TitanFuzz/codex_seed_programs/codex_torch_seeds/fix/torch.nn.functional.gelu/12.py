'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gelu\ntorch.nn.functional.gelu(input)\n'
import torch
import torch.nn.functional as F
input = torch.randn(2, 3)
print('Input: ', input)
output = F.gelu(input)
print('Output: ', output)
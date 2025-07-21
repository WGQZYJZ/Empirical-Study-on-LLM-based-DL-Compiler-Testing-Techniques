'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.corrcoef\ntorch.corrcoef(input)\n'
import torch
input = torch.randn(4, 4)
print('Input: \n', input)
output = torch.corrcoef(input)
print('Output: \n', output)
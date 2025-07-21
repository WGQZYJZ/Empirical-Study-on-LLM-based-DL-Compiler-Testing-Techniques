'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.corrcoef\ntorch.corrcoef(input)\n'
import torch
input = torch.randn(3, 3)
print('input: ', input)
output = torch.corrcoef(input)
print('output: ', output)
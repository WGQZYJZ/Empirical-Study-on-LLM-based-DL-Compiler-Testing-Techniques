'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.corrcoef\ntorch.corrcoef(input)\n'
import torch
x = torch.randn(3, 3)
print('input data: ', x)
y = torch.corrcoef(x)
print('corrcoef result: ', y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
result = torch.argsort(x, dim=(- 1), descending=False)
print('The result is: ', result)
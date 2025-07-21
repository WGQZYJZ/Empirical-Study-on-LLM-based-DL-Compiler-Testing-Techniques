'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
mask = input.ge(0.5)
result = torch.masked_select(input, mask)
print(input)
print(mask)
print(result)
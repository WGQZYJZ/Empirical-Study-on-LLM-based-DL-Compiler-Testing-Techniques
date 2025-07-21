'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
input = torch.randn(3, 4)
mask = torch.ByteTensor([0, 1, 1, 0])
print(torch.masked_select(input, mask))
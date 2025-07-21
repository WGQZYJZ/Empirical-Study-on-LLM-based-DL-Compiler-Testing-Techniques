'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
input = torch.randn(3, 4)
input
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 1]])
mask
torch.masked_select(input, mask)
'\nTask 4: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
input = torch.randn(3, 4)
input
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 1]])
mask
out = torch.masked_select(input, mask)
out
'\nTask 5: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
input = torch.randn(3, 4)
input
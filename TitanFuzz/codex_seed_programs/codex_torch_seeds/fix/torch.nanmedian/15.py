'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
output = torch.nanmedian(input)
print(output)
output = torch.nanmedian(input, dim=0)
print(output)
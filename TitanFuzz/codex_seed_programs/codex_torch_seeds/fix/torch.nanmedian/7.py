'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=torch.float32)
output = torch.nanmedian(input, dim=(- 1), keepdim=False, out=None)
print(output)
output = torch.nanmedian(input, dim=(- 1), keepdim=True, out=None)
print(output)
output = torch.nanmedian(input, dim=1, keepdim=False, out=None)
print(output)
output = torch.nanmedian(input, dim=1, keepdim=True, out=None)
print(output)
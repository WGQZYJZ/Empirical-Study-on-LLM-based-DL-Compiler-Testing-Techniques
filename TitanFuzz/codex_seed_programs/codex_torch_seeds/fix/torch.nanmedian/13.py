'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(2, 3)
print(data)
print(torch.median(data))
print(torch.median(data, dim=0))
print(torch.median(data, dim=1))
print(torch.median(data, dim=1, keepdim=True))
print(torch.nanmedian(data))
print(torch.nanmedian(data, dim=0))
print(torch.nanmedian(data, dim=1))
print(torch.nanmedian(data, dim=1, keepdim=True))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(torch.amax(data, dim=0))
print(torch.amax(data, dim=1))
print(torch.amax(data, dim=1, keepdim=True))
print(torch.amax(data, dim=0, keepdim=True))
print(torch.amax(data, dim=(- 1)))
print(torch.amax(data, dim=(- 1), keepdim=True))
print(torch.amax(data, dim=(- 2)))
print(torch.amax(data, dim=(- 2), keepdim=True))
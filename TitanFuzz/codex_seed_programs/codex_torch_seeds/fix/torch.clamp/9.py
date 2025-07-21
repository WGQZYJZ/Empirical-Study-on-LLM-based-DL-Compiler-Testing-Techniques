'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
import torch
data = torch.randn(100)
torch.clamp(data, min=(- 0.5), max=0.5)
torch.clamp(data, min=(- 0.5), max=0.5, out=data)
data.clamp_((- 0.5), 0.5)
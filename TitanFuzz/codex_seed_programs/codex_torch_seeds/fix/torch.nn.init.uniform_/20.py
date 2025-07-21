'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
data = torch.rand(2, 3)
print(data)
torch.nn.init.uniform_(data, a=(- 1.0), b=1.0)
print(data)
data = torch.rand(2, 3)
print(data)
torch.nn.init.uniform_(data, a=(- 1.0))
print(data)
data = torch.rand(2, 3)
print(data)
torch.nn.init.uniform_(data)
print(data)
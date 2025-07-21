'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
data = torch.randn(2, 3, 4)
print(data)
print(data.shape)
print(torch.squeeze(data))
print(torch.squeeze(data, dim=1))
print(torch.squeeze(data, dim=2))
print(torch.squeeze(data, dim=0))
print(torch.squeeze(data, dim=1).shape)
print(torch.squeeze(data, dim=2).shape)
print(torch.squeeze(data, dim=0).shape)
'\ntorch.unsqueeze(input, dim, out=None)\n'
'\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
data = torch.tensor([[True, True, True, True], [True, True, True, True]])
torch.all(data)
torch.all(data, dim=0)
torch.all(data, dim=0, keepdim=True)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
input = torch.tensor([1, 2, 3, 4])
print(torch.unsqueeze(input, 0))
print(torch.unsqueeze(input, 1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim)\n'
import torch
input = torch.tensor([[1], [2], [3], [4]])
print(torch.squeeze(input, 0))
print(torch.squeeze(input, 1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
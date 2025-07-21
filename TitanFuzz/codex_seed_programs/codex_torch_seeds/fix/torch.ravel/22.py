'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
arr = torch.randn(3, 3)
print(arr)
print(torch.ravel(arr))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input)\n'
import torch
arr = torch.randn(3, 3)
print(arr)
print(torch.flatten(arr))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
arr = torch.randn(3, 3)
print(arr)
print(torch.flatten(arr, start_dim=1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
arr = torch
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output = torch.mean(input, dim=1)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output = torch.mean(input, dim=1, keepdim=True)
print(output)
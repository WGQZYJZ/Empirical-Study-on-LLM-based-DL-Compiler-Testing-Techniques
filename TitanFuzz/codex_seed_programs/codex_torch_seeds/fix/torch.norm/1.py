"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
import torch
input = torch.randn(3, 5)
print(input)
output = torch.norm(input, p=2, dim=1, keepdim=False, out=None, dtype=None)
print(output)
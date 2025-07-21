'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 5)
print(input)
(max_value, max_idx) = torch.max(input, dim=1)
print(max_value)
print(max_idx)
(max_value, max_idx) = torch.max(input, dim=1, keepdim=True)
print(max_value)
print(max_idx)
(max_value, max_idx) = torch.max(input, dim=1, keepdim=True, out=(torch.zeros(3, 1), torch.zeros(3, 1, dtype=torch.long)))
print(max_value)
print(max_idx)
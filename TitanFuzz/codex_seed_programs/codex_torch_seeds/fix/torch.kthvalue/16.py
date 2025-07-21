'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(3, 4)
print(data)
(value, index) = torch.kthvalue(data, 2, 1)
print(value)
print(index)
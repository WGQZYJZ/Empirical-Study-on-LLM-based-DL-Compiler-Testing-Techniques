'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3, requires_grad=True)
other = torch.randn(3, 4, requires_grad=True)
result = torch.matmul(input, other)
print(result)
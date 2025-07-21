'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 5, requires_grad=True)
other = torch.randn(5, 6, requires_grad=True)
output = torch.matmul(input, other)
print(output)
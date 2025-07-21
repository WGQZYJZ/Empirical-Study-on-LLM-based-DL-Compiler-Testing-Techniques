'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addr\ntorch.addr(input, vec1, vec2, *, beta=1, alpha=1, out=None)\n'
import torch
input = torch.randn(3, 3, requires_grad=True)
vec1 = torch.randn(3, requires_grad=True)
vec2 = torch.randn(3, requires_grad=True)
output = torch.addr(input, vec1, vec2)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(tensor, value=1, tensor1, tensor2, *, out=None)\n'
import torch
input = torch.randn(3, 3, requires_grad=True)
vec1 = torch.randn(3, requires_grad=True)
vec2 = torch.randn(3, requires_grad=True)
output = torch.addcdiv(input, 1, vec1, vec2)
print(output)
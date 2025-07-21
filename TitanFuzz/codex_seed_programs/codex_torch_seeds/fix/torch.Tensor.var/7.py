'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor.var(dim=0))
print(input_tensor.var(dim=1))
print(input_tensor.var(dim=0, unbiased=False))
print(input_tensor.var(dim=1, unbiased=False))
print(input_tensor.var(dim=0, keepdim=True))
print(input_tensor.var(dim=1, keepdim=True))
print(input_tensor.var(dim=1, unbiased=False, keepdim=True))
print(torch.var(input_tensor))
print(torch.var(input_tensor, unbiased=False))
print(torch.var(input_tensor, dim=0))
print(torch.var(input_tensor, dim=1))
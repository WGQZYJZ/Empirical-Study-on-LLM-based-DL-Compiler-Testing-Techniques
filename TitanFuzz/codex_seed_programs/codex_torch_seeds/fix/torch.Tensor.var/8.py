'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
print(input_tensor.var(dim=0, unbiased=True, keepdim=False))
print(input_tensor.var(dim=1, unbiased=True, keepdim=False))
print(input_tensor.var(dim=0, unbiased=True, keepdim=True))
print(input_tensor.var(dim=1, unbiased=True, keepdim=True))
print(input_tensor.var(dim=0, unbiased=False, keepdim=False))
print(input_tensor.var(dim=1, unbiased=False, keepdim=False))
print(input_tensor.var(dim=0, unbiased=False, keepdim=True))
print(input_tensor.var(dim=1, unbiased=False, keepdim=True))
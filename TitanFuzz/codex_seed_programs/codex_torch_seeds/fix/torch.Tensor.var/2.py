'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.rand(4, 4)
print(input_tensor)
var_tensor = input_tensor.var(dim=0, unbiased=True, keepdim=False)
print(var_tensor)
var_tensor = input_tensor.var(dim=1, unbiased=True, keepdim=False)
print(var_tensor)
var_tensor = input_tensor.var(dim=0, unbiased=True, keepdim=True)
print(var_tensor)
var_tensor = input_tensor.var(dim=1, unbiased=True, keepdim=True)
print(var_tensor)
var_tensor = input_tensor.var(dim=0, unbiased=False, keepdim=False)
print(var_tensor)
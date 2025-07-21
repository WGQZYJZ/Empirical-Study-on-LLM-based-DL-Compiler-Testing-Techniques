'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor: ', input_tensor)
var_value = input_tensor.var(dim=0, unbiased=True, keepdim=False)
print('var_value: ', var_value)
print('\n')
var_value = input_tensor.var(dim=1, unbiased=True, keepdim=False)
print('var_value: ', var_value)
print('\n')
var_value = input_tensor.var(dim=1, unbiased=False, keepdim=False)
print('var_value: ', var_value)
print('\n')
var_value = input_tensor.var(dim=1, unbiased=True, keepdim=True)
print('var_value: ', var_value)
print('\n')
var_value = input_tensor
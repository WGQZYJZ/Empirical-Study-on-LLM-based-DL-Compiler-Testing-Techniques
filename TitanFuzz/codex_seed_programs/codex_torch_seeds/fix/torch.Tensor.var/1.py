'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
var_output = input_tensor.var(dim=0, unbiased=False, keepdim=False)
print('Input tensor: \n', input_tensor)
print('Output tensor: \n', var_output)
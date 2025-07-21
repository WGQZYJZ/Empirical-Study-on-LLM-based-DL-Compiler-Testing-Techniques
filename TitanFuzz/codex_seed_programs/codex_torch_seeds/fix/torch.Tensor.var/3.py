'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
import torch
_input_tensor = torch.rand(3, 3)
_var = torch.Tensor.var(_input_tensor, dim=None, unbiased=True, keepdim=False)
print(_var)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.rand(10, 20)
print(_input_tensor.any())
print(_input_tensor.any(dim=0))
print(_input_tensor.any(dim=1))
print(_input_tensor.any(dim=0, keepdim=True))
print(_input_tensor.any(dim=1, keepdim=True))
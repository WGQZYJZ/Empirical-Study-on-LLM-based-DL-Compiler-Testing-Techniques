'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.max\ntorch.Tensor.max(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.rand(10, 10)
_max_output = torch.Tensor.max(_input_tensor, dim=None, keepdim=False)
print(_max_output)
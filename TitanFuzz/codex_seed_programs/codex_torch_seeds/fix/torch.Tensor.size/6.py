'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.size\ntorch.Tensor.size(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.rand(3, 4)
print(_input_tensor.size(0))
print(_input_tensor.size(1))
print(_input_tensor.size())
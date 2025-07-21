'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.size\ntorch.Tensor.size(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.randn(3, 5)
print(_input_tensor.size())
print(_input_tensor.size(0))
print(_input_tensor.size(1))
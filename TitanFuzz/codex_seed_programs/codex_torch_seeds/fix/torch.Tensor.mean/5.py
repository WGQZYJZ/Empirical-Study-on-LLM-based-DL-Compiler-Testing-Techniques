'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.rand(3, 3)
_mean_tensor = _input_tensor.mean(dim=None, keepdim=False, dtype=None)
print(_mean_tensor)
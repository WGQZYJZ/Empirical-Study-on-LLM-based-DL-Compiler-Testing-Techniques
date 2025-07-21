'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.rand(1, 2, 3)
_result = _input_tensor.sum(dim=1)
print(_result)
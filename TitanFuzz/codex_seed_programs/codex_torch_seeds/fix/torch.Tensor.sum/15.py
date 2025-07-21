'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.rand(4, 4)
_output_tensor = _input_tensor.sum(dim=0, keepdim=True)
print(_output_tensor)
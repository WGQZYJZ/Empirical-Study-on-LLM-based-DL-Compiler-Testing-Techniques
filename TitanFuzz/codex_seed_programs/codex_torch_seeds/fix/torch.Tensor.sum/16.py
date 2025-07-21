'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)
print('_input_tensor:', _input_tensor)
print('_output_tensor:', _output_tensor)
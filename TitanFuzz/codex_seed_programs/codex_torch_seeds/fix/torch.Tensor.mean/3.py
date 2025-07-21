'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input Tensor: \n', _input_tensor)
_output_tensor = _input_tensor.mean(dim=1, keepdim=True)
print('Output Tensor: \n', _output_tensor)
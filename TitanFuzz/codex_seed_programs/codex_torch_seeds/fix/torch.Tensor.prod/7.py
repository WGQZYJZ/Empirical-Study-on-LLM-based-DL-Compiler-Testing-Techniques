'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.prod\ntorch.Tensor.prod(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = _input_tensor.prod(dim=1, keepdim=True)
print('Input Tensor:', _input_tensor)
print('Output Tensor:', _output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.prod\ntorch.Tensor.prod(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = _input_tensor.prod(dim=0, keepdim=True)
print('input tensor:', _input_tensor)
print('output tensor:', _output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.prod\ntorch.Tensor.prod(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = _input_tensor.prod(dim=0, keepdim=False)
print
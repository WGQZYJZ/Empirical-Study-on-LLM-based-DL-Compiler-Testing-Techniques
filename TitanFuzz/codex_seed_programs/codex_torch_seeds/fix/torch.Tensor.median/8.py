'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print(_input_tensor)
_output_tensor = _input_tensor.median()
print(_output_tensor)
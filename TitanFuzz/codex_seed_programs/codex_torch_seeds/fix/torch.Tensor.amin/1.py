'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input Tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.amin(dim=0, keepdim=False)
print('Output Tensor: {}'.format(_output_tensor))
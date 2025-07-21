'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print('Input Tensor: {}'.format(_input_tensor))
print('Is the input tensor complex? {}'.format(_input_tensor.is_complex()))
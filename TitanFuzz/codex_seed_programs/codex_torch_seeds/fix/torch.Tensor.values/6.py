'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.values\ntorch.Tensor.values(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = _input_tensor.values()
print('input tensor: {}'.format(_input_tensor))
print('output tensor: {}'.format(_output_tensor))
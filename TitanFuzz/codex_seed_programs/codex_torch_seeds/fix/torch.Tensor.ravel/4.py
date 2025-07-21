'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = _input_tensor.ravel()
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)
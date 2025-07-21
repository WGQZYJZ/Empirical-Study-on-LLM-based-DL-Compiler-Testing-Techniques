'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 3)
_output_tensor = _input_tensor.ravel()
print('input tensor: ', _input_tensor)
print('output tensor: ', _output_tensor)
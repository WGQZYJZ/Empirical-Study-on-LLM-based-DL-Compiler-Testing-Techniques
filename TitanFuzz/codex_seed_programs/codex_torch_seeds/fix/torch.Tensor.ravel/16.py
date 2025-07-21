'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 4, 4)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.ravel(_input_tensor)
print('Output tensor: ', _output_tensor)
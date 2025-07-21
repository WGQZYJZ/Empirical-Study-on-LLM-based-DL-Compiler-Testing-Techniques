'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
_input_tensor = torch.randn(4, 4)
print('Input tensor: ', _input_tensor)
'\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
_output_tensor = torch.Tensor.isinf(_input_tensor)
print('Output tensor: ', _output_tensor)
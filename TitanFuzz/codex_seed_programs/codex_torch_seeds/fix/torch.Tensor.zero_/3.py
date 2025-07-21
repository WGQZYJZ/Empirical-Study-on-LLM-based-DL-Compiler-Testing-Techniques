'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.zero_\ntorch.Tensor.zero_(_input_tensor)\n'
import torch
_input_data = torch.randn(2, 3)
print('Input data:')
print(_input_data)
_input_tensor = torch.Tensor.zero_(_input_data)
print('Output tensor:')
print(_input_tensor)
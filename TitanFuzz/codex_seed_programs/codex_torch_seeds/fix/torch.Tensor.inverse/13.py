'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inverse\ntorch.Tensor.inverse(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.inverse(_input_tensor)
print('Output tensor:')
print(_output_tensor)
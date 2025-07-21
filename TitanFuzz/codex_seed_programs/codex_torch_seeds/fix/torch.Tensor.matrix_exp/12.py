'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_exp\ntorch.Tensor.matrix_exp(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.matrix_exp(_input_tensor)
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(_output_tensor)
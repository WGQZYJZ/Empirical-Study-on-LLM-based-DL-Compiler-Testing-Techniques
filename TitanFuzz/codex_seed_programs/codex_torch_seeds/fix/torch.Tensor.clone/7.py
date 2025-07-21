'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
_input_tensor = torch.randn(3, 3)
print('Input tensor:')
print(_input_tensor)
print('Task 3: Call the API torch.Tensor.clone')
_output_tensor = _input_tensor.clone()
print('Output tensor:')
print(_output_tensor)
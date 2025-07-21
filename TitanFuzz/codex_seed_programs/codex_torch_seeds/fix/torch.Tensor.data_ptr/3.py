'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.data_ptr\ntorch.Tensor.data_ptr(_input_tensor)\n'
import torch
_input_tensor = torch.randn(5, 3)
print('Input tensor:')
print(_input_tensor)
print('\nAddress of the input tensor:')
print(torch.Tensor.data_ptr(_input_tensor))
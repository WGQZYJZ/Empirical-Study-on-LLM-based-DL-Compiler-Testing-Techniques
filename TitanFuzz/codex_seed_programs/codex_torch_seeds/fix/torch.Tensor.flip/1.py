'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
_input_tensor = torch.randn(3, 4)
print('input tensor: ', _input_tensor)
print('Task 3: Call the API torch.Tensor.flip')
_output_tensor = torch.Tensor.flip(_input_tensor, dims=(0, 1))
print('output tensor: ', _output_tensor)
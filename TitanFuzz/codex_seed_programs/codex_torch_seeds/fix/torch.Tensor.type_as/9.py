'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('The input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.type_as(torch.IntTensor())
print('The output tensor: {}'.format(_output_tensor))
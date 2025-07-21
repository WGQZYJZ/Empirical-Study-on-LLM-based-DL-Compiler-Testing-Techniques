'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = _input_tensor.numpy()
print('input tensor: {}'.format(_input_tensor))
print('output tensor: {}'.format(_output_tensor))
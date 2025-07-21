'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log\ntorch.Tensor.log(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 3)
_output_tensor = torch.Tensor.log(_input_tensor)
print('input tensor: {}'.format(_input_tensor))
print('output tensor: {}'.format(_output_tensor))
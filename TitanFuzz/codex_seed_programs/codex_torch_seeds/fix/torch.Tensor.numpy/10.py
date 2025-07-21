'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = _input_tensor.numpy()
print('The input tensor is: {}'.format(_input_tensor))
print('The output tensor is: {}'.format(_output_tensor))
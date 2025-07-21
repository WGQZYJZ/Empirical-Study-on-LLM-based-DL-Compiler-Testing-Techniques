'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.sign()
print('Output tensor: {}'.format(_output_tensor))
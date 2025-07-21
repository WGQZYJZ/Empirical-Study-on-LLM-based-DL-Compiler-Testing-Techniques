'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: \n{}'.format(_input_tensor))
_output_tensor = _input_tensor.sign()
print('Output tensor: \n{}'.format(_output_tensor))
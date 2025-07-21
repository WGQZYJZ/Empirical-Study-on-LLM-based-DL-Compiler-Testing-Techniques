'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 4)
_output_tensor = torch.Tensor.signbit(_input_tensor)
print('Input Tensor:\n{}\n'.format(_input_tensor))
print('Output Tensor:\n{}'.format(_output_tensor))
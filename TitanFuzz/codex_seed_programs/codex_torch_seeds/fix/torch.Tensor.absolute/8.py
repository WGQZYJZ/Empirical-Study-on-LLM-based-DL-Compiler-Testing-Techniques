'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.absolute\ntorch.Tensor.absolute(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.absolute(_input_tensor)
print('Input tensor:\n{}\n'.format(_input_tensor))
print('Output tensor:\n{}'.format(_output_tensor))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative\ntorch.Tensor.negative(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input data: \n{}'.format(_input_tensor))
_output_tensor = torch.Tensor.negative(_input_tensor)
print('Output data: \n{}'.format(_output_tensor))
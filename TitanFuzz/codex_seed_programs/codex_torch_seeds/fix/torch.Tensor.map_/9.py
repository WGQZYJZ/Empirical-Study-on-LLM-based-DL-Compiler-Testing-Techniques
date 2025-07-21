'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.map_\ntorch.Tensor.map_(_input_tensor, tensor, callable\n'
import torch
from torch.autograd import Variable
import torch
_input_tensor = torch.FloatTensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.map_(_input_tensor, _input_tensor, (lambda x, y: (x + y)))
print('Input Tensor:\n{}'.format(_input_tensor))
print('Output Tensor:\n{}'.format(_output_tensor))
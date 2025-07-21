'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.values\ntorch.Tensor.values(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
_input_tensor = torch.rand(10, 20)
_input_tensor_variable = Variable(_input_tensor)
_output_tensor = _input_tensor_variable.values()
print('input_tensor: ', _input_tensor)
print('input_tensor_variable: ', _input_tensor_variable)
print('output_tensor: ', _output_tensor)
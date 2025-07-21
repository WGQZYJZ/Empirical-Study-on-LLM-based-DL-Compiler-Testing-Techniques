'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
from torch.autograd import Variable
_input_tensor = Variable(torch.rand(3, 4))
_output_tensor = _input_tensor.t()
print(_output_tensor)
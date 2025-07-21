import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.FloatTensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.map_(_input_tensor, _input_tensor, (lambda x, y: (x + y)))
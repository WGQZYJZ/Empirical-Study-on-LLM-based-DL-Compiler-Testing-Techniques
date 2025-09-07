import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.map_(tensor, _input_tensor, (lambda x, y: (x + y)))
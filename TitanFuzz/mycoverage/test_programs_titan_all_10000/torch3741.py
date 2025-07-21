import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
torch.Tensor.apply_(_input_tensor, (lambda x: print(x)))
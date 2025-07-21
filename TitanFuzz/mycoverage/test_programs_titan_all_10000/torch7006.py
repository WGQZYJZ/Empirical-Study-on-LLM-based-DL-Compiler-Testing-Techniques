import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
torch.Tensor.copy_(_input_tensor, src=torch.rand(2, 3))
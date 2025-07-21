import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
other_tensor = torch.rand(2, 3)
torch.Tensor.less_equal_(input_tensor, other_tensor)
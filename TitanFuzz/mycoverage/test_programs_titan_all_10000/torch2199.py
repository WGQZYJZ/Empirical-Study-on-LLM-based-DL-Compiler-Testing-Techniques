import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
data = torch.rand(2, 3)
torch.Tensor.new_tensor(_input_tensor, data)
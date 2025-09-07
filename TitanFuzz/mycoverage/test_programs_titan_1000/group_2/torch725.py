import torch
from torch import nn
from torch.autograd import Variable
input_tensor = Variable(torch.rand(2, 3))
other_tensor = Variable(torch.rand(2, 3))
torch.Tensor.xlogy(input_tensor, other_tensor)
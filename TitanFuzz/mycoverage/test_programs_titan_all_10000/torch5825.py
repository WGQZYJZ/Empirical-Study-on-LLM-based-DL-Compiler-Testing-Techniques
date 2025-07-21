import torch
from torch import nn
from torch.autograd import Variable
input_tensor = Variable(torch.rand(3, 5))
torch.Tensor.sin_(input_tensor)
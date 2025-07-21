import torch
from torch import nn
from torch.autograd import Variable
input_tensor = Variable(torch.randn(2, 3, 3, 3))
torch.Tensor.dense_dim(input_tensor)
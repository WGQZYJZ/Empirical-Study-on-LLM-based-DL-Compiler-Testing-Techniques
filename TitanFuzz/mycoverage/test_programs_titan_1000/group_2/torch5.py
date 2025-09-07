import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.Tensor([1]), requires_grad=True)
y = torch.nn.Sigmoid()(x)
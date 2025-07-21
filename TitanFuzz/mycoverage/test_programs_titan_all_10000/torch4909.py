import torch
from torch import nn
from torch.autograd import Variable
input_tensor = Variable(torch.randn(2, 2))
symeig_output = torch.Tensor.symeig(input_tensor, eigenvectors=True, upper=True)
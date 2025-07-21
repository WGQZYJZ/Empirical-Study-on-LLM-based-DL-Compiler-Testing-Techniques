import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.randn(2, 3)
input2 = torch.randn(3, 2)
output = torch.einsum('ij,jk->ik', input1, input2)
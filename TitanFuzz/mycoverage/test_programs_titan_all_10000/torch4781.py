import torch
from torch import nn
from torch.autograd import Variable
A = Variable(torch.randn(3, 5))
pinv_A = torch.linalg.pinv(A)
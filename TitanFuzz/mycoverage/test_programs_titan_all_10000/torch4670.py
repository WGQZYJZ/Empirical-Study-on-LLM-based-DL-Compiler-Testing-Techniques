import torch
from torch import nn
from torch.autograd import Variable
if True:
    x = torch.randn(4)
    print('Input:', x)
    print('Output:', torch.atan(x))
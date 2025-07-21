import torch
from torch import nn
from torch.autograd import Variable
if True:
    x = torch.randn(3, 4)
    y = torch.randn(4, 5)
    print(torch.matmul(x, y))
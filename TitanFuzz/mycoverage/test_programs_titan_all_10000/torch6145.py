import torch
from torch import nn
from torch.autograd import Variable
if True:
    input = torch.randn(3, 3)
    print('Input data:')
    print(input)
    print('Result of torch.cummax:')
    print(torch.cummax(input, dim=0))
    print(torch.cummax(input, dim=1))
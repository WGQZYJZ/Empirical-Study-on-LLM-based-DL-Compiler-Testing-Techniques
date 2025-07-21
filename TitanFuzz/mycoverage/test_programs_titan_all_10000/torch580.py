import torch
from torch import nn
from torch.autograd import Variable
if True:
    input = torch.randn(2, 3)
    print('Input: ', input)
    print('Output: ', torch.special.gammaln(input))
import torch
from torch import nn
from torch.autograd import Variable

if True:
    input = torch.randn(4, 4)
    output = torch.special.erf(input)
    print(output)
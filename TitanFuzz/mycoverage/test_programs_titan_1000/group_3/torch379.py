import torch
from torch import nn
from torch.autograd import Variable
if True:
    input = torch.randn(10, 10, dtype=torch.float)
    print(torch.special.exp2(input))
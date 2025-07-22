import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x1 = torch.cat((x, x), dim=1)
        x1 = torch.unsqueeze(x1, 0)
        if (not (x1.size() == (1, 10, 3, 4))):
            x1 = x1.resize(1, 10, 3, 4)
        x2 = torch.cat((x1, x1), dim=3)
        x3 = torch.cat((x1, x1), dim=3)
        x4 = torch.cat((x1, x1), dim=3)
        x4_tranposed = x4.transpose(0, 1)
        return torch.cat((x1, x2, x3, x4, x4_tranposed), dim=0).permute(3, 1, 2, 0).contiguous().view(3, (- 1))




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
requested resize to 1x10x3x4 (120 elements in total), but the given tensor has a size of 1x2x6x4 (48 elements). autograd's resize can only change the shape of a given tensor, while preserving the number of elements. 

jit:
Failed running call_method resize(*(FakeTensor(..., device='cuda:0', size=(1, 2, 6, 4)), 1, 10, 3, 4), **{}):
requested resize to 1x10x3x4 (120 elements in total), but the given tensor has a size of 1x2x6x4 (48 elements). autograd's resize can only change the shape of a given tensor, while preserving the number of elements. 

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
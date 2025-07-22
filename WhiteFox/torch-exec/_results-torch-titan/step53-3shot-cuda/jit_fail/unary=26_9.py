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
        self.conv_t = torch.nn.ConvTranspose2d(527, 6, 8, stride=19, padding=0, bias=False)

    def forward(self, x2):
        g2 = self.conv_t(x2)
        g3 = (g2 > 0)
        g4 = (g2 * 2.63601)
        g5 = torch.where(g3, torch.transpose(g4, 4, 3), ((- 1.31601) * torch.transpose(g4, 4, 3)))
        return torch.transpose(g5, 4, 3)




func = Model().to('cuda')



x2 = torch.randn(195, 527, 117, 1)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-4, 3], but got 4)

jit:
Failed running call_function <built-in method transpose of type object at 0x75d60a4699e0>(*(FakeTensor(..., device='cuda:0', size=(195, 6, 2212, 8)), 4, 3), **{}):
Dimension out of range (expected to be in range of [-4, 3], but got 4)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
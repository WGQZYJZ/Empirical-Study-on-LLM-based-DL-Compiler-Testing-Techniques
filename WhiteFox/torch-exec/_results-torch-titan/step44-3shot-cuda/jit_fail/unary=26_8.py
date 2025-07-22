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
        self.conv_t = torch.nn.ConvTranspose2d(4, 6, 5, padding=2, stride=1)
        self.negative_slope = 0.2

    def forward(self, x3):
        m1 = self.conv_t(x3)
        m2 = (m1 > 0)
        m3 = (m1 * self.negative_slope)
        m4 = torch.where(m2, m1, m3)
        return torch.nn.functional.dropout(m4, p=0.3850582905077984, train=False)




func = Model().to('cuda')



x3 = torch.randn(5, 4, 83, 76)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
dropout() got an unexpected keyword argument 'train'

jit:
Failed running call_function <function dropout at 0x7555b96a08b0>(*(FakeTensor(..., device='cuda:0', size=(5, 6, 83, 76)),), **{'p': 0.3850582905077984, 'train': False}):
dropout() got an unexpected keyword argument 'train'

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
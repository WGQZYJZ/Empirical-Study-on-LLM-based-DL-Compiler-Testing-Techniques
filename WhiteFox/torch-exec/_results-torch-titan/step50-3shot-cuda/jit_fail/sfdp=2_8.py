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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9):
        q = self.multihead_attention(query=x1, key=x2, value=x3)
        l = self.multihead_attention(query=q, key=x4, value=x5)
        m = self.multihead_attention(query=l, key=x6, value=x7)
        n = self.multihead_attention(query=m, key=x8, value=x9)
        return n



func = Model().to('cuda')



x1 = torch.rand(1, 16, 256)



x2 = torch.rand(1, 24, 256)



x3 = torch.rand(1, 24, 256)



x4 = torch.rand(1, 28, 108)



x5 = torch.rand(1, 28, 108)



x6 = torch.rand(1, 32, 54)



x7 = torch.rand(1, 32, 54)



x8 = torch.rand(1, 36, 27)



x9 = torch.rand(1, 36, 27)


test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'multihead_attention'

jit:
multihead_attention

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
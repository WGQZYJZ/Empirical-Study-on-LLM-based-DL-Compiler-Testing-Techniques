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

    def forward(self, x1):
        v1 = x1.size(0)
        v2 = x1.size(1)
        v3 = x1.size(2)
        v4 = x1.size(3)
        v5 = torch.matmul(x1.view(v1, v2, (v3 * v4)), x1.view(v2, v1, (v3 * v4)).transpose(1, 2))
        v5 = (v5 / math.sqrt((v3 * v4)))
        v6 = (v5 + attn_mask)
        v7 = torch.softmax(v6, dim=(- 1))
        y__ = torch.matmul(v7, x1)
        return y__



func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'size'

jit:
'int' object has no attribute 'size'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
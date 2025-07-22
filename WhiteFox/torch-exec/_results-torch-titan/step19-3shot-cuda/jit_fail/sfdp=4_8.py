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

    def __init__(self, natt, ninp):
        super().__init__()
        self.register_buffer('am', torch.zeros((1, natt, 1, 1), dtype=torch.bool))

    def forward(self, x1, x2):
        attn = ((x1 @ x2.transpose((- 2), (- 1))) / math.sqrt(x1.shape[(- 1)]))
        attn = (attn + self.am)
        attn = torch.softmax(attn, dim=(- 1))
        output = (attn @ x2)
        return output



natt = 1
ninp = 1
func = Model(4, 16).to('cuda')



x1 = torch.randn(1, 4, 8, 16)

x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
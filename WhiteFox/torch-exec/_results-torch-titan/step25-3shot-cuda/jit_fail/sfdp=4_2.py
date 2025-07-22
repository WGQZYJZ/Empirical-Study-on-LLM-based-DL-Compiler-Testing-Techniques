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

    def forward(self, x14):
        v7 = x14.transpose((- 2), (- 1))
        v8 = (x14 @ v7)
        v9 = (v8 / math.sqrt(x14.size((- 1))))
        v10 = (v9 + x9)
        v11 = torch.softmax(v10, dim=(- 1))
        v12 = (x14 @ v11)
        return v12



func = Model().to('cuda')



x14 = torch.randn(1, 64, 64)


test_inputs = [x14]

# JIT_FAIL
'''
direct:
name 'x9' is not defined

jit:
name 'x9' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
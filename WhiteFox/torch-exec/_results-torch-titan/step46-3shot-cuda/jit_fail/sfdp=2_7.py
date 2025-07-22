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
        v1 = torch.matmul(x2, x3.transpose((- 2), (- 1)))
        v2 = (v1 / inv_scale_factor)
        v3 = torch.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = torch.matmul(v4, v6)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'x3' is not defined

jit:
name 'x3' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
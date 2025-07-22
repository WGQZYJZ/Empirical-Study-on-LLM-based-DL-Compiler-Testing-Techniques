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

    def forward(self, x1, x2, d_p):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)), dim=(- 1))
        v2 = v1.div(0.5)
        v3 = torch.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=d_p, training=False)
        v5 = v4.matmul(x2)
        return v5



func = Model().to('cuda')



x1 = torch.randn(2, 4, 64)



x2 = torch.randn(2, 64, 100)

d_p = 1

test_inputs = [x1, x2, d_p]

# JIT_FAIL
'''
direct:
matmul() got an unexpected keyword argument 'dim'

jit:
Failed running call_function <built-in method matmul of type object at 0x77d7ce2699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 4, 64)), FakeTensor(..., device='cuda:0', size=(2, 100, 64))), **{'dim': -1}):
matmul() got an unexpected keyword argument 'dim'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
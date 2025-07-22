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
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat((v1, v1, v1, v1, v1), 2)
        v3 = v2.squeeze((- 1))
        v4 = v3.view(((- 1), 16))
        return (v3 + v4)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 16]' is invalid for input of size 20

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 2, 10)), (-1, 16)), **{}):
shape '[-1, 16]' is invalid for input of size 20

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
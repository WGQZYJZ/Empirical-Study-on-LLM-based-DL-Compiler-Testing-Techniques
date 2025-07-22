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

    def forward(self, x1, x2):
        v0 = x2.permute(0, 2, 1)
        v1 = torch.bmm(X1, v0)
        v2 = torch.bmm(v0, X1)
        v3 = (v1.permute(0, 1, 2) * v2.permute(1, 2, 0)).permute(0, 2, 1)
        v4 = torch.cat((v3, X2), 1)[(..., 0)]
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'X1' is not defined

jit:
name 'X1' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
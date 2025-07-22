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
        self.op1 = torch.squeeze
        self.op2 = torch.mean
        self.op3 = torch.add

    def forward(self, x):
        v1 = self.op1(x)
        v2 = self.op2(v1)
        v3 = self.op3(v2)
        return v3




func = Model().to('cuda')



x = torch.randn(16, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
add() received an invalid combination of arguments - got (Tensor), but expected (Tensor input, Tensor other, *, Number alpha, Tensor out)

jit:
Failed running call_function <built-in method add of type object at 0x7673ea6699e0>(*(FakeTensor(..., device='cuda:0', size=()),), **{}):
add() received an invalid combination of arguments - got (FakeTensor), but expected (Tensor input, Tensor other, *, Number alpha, Tensor out)

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
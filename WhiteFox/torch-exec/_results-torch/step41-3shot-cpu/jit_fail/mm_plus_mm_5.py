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

    def forward(self, in1, in2, in3, in4):
        t0 = torch.mm(in1, in2)
        t1 = torch.mm(in3, in4)
        t2 = torch.mm(in4, in5)
        t0 += t1
        t2 += t1
        t0 += torch.mm(in5, in6)
        t2 += t2
        return t0 + t2



func = Model().to('cpu')


in1 = torch.randn(6, 6)

in2 = torch.randn(6, 6)

in3 = torch.randn(6, 6)

in4 = torch.randn(6, 6)

test_inputs = [in1, in2, in3, in4]

# JIT_FAIL
'''
direct:
name 'in5' is not defined

jit:
NameError: name 'in5' is not defined

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
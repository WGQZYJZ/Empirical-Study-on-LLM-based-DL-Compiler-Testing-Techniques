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
        o1 = torch.nn.functional.linear(x1, x2[0], x2[1], bias=x2[2])
        o2 = torch.relu(o1)
        return o2



func = Model().to('cuda')



in_data1 = torch.rand(1, 7)

x1 = 1

test_inputs = [in_data1, x1]

# JIT_FAIL
'''
direct:
'int' object is not subscriptable

jit:
'int' object is not subscriptable

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
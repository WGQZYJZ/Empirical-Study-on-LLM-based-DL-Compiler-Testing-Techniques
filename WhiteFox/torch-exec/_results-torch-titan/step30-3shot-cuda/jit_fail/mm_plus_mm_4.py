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

    def forward(self, t1, t2):
        tt1 = torch.mm(t1, t1)
        tt2 = torch.mm(t2, t2)
        tt3 = (torch.mm(tt1, tt2) + 12)
        return (tt1.mm(tt2) + tt3)




func = Model().to('cuda')



t1 = torch.randn(1, 1, 1, 100, 100)



t2 = torch.randn(1, 1, 1, 100, 100)


test_inputs = [t1, t2]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x74f81dc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 100, 100)), FakeTensor(..., device='cuda:0', size=(1, 1, 1, 100, 100))), **{}):
a must be 2D

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
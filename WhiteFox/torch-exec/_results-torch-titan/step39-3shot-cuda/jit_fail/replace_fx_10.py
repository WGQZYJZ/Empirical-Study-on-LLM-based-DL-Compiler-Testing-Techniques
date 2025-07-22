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

    def forward(self, x):
        x1 = torch.nn.functional.dropout(x, p=0.37)
        x2 = torch.nn.functional.dropout(x, p=0.28)
        x3 = torch.nn.functional.dropout(x, p=0.73)
        x4 = torch.nn.functional.dropout(x, p=0.52)
        return (((torch.mm(x1, x2) - x3) - x4) + 2.0)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x79cc286699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2))), **{}):
a must be 2D

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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



class M(nn.Module):

    def __init__(self):
        super(M, self).__init__()
        self.fc1 = nn.Linear(10, 42)

    def forward(self, x):
        y1 = self.fc1(x)
        y2 = self.fc1(x)
        y3 = self.fc1(x)
        y3 = torch.mm(y3, y3)
        y4 = torch.mm(y3, y4)
        return (((y1 + y2) + y3) + y4)




func = M().to('cuda')



x = torch.randn(10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x78625e6699e0>(*(FakeTensor(..., device='cuda:0', size=(42,)), FakeTensor(..., device='cuda:0', size=(42,))), **{}):
a must be 2D

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
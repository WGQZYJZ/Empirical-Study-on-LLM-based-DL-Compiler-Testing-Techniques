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



class model(torch.nn.Module):

    def __init__(self):
        super(model, self).__init__()

    def forward(self, x1, x2):
        t1 = torch.nn.functional.relu(x1)
        t2 = torch.nn.functional.max_pool2d(t1, 2)
        t3 = torch.nn.functional.relu(t2)
        t4 = torch.nn.functional.max_pool2d(t3, 1)
        t5 = torch.nn.functional.relu(t4)
        t6 = torch.nn.functional.max_pool2d(t5, 1)
        (t7, _) = torch.max(t6, 1)
        t8 = torch.mean(t7, 1)
        t9 = (t6 + torch.reshape(t8, ((- 1), 1, 1, 1024)))
        t10 = torch.nn.functional.relu(t9)
        u1 = torch.nn.functional.relu(x2)
        u2 = torch.nn.functional.max_pool2d(u1, 2)
        u3 = torch.nn.functional.relu(u2)
        u4 = torch.nn.functional.max_pool2d(u3, 1)
        u5 = torch.nn.functional.relu(u4)
        u6 = torch.nn.functional.max_pool2d(u3, 1)
        (u7, _) = torch.max(u6, 1)
        u8 = torch.mean(u7, 1)
        u9 = (u6 + torch.reshape(u8, ((- 1), 1, 1, 1024)))
        u10 = torch.nn.functional.relu(u9)
        return ((t10 + u10), (t10 * u10), (t10 - u10))




func = model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)



x2 = torch.randn(1, 1, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
shape '[-1, 1, 1, 1024]' is invalid for input of size 32

jit:
Failed running call_function <built-in method reshape of type object at 0x74f814e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 32)), (-1, 1, 1, 1024)), **{}):
shape '[-1, 1, 1, 1024]' is invalid for input of size 32

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
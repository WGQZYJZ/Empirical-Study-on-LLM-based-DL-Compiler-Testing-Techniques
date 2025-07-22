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
        v = torch.mm(x1, x2)
        for _ in range(10):
            v = torch.mm(x1, x2)
        return torch.cat([v, v, v, v, v, v, v, v, v, v, v, v, v, v, v], 2)




func = Model().to('cuda')



x1 = torch.randn(4, 4)



x2 = torch.randn(4, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 2)

jit:
Failed running call_function <built-in method cat of type object at 0x766981e699e0>(*([FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4))], 2), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
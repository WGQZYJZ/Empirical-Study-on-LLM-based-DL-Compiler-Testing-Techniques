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

    def forward(self, x1, x2, inp1):
        v1 = torch.mm(x1, x2)
        v2 = v1[inp1, :]
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 25)



x2 = torch.randn(25, 7)



inp = torch.randn(1, 25)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
tensors used as indices must be long, int, byte or bool tensors

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 7)), (FakeTensor(..., device='cuda:0', size=(1, 25)), slice(None, None, None))), **{}):
tensors used as indices must be long, int, byte or bool tensors

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, x1):
        b = x1.shape[0]
        c = 2
        m = x1.shape[1]
        v1 = torch.addmm(x1, torch.ones(b, c, m, device='cuda'))
        return torch.cat([v1, v1])



func = Model().to('cuda')



x1 = torch.randn(3, 2, device='cuda')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
addmm() received an invalid combination of arguments - got (Tensor, Tensor), but expected (Tensor input, Tensor mat1, Tensor mat2, *, Number beta, Number alpha, Tensor out)

jit:
Failed running call_function <built-in method addmm of type object at 0x70adc8a699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 2)), FakeTensor(..., device='cuda:0', size=(3, 2, 2))), **{}):
addmm() received an invalid combination of arguments - got (FakeTensor, FakeTensor), but expected (Tensor input, Tensor mat1, Tensor mat2, *, Number beta, Number alpha, Tensor out)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
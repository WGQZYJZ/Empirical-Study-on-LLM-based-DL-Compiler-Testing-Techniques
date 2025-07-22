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
        self.softmax = torch.nn.Softmax(dim=(- 2))

    def forward(self, q, k, v, a):
        d = q.size((- 2))
        scale = torch.sqrt(k.size((- 1)))
        qk = ((q @ k.transpose((- 2), (- 1))) / scale)
        qk = (qk + a)
        attn_w = self.softmax(qk)
        output = (attn_w @ v)
        return (output, attn_w.sum())



func = Model().to('cuda')



q = torch.randn(5, 3, 64)



k = torch.randn(6, 5, 64)



v = torch.randn(7, 6, 20)



a = torch.randn(6, 6)


test_inputs = [q, k, v, a]

# JIT_FAIL
'''
direct:
sqrt(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method sqrt of type object at 0x703517e699e0>(*(64,), **{}):
sqrt(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
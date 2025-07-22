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

    def forward(self, x1, x2, x3, x4):
        q = x1
        k = x2
        v = x3
        s = x4
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = torch.sqrt(q.size((- 1))).to(s)
        qk_scaled = qk.div(inv_scale_factor)
        softmax_qk = qk_scaled.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 2, 1024)



x2 = torch.randn(1, 2, 1024)



x3 = torch.randn(1, 2, 1024)



x4 = torch.randn(1, 2, 1024)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
sqrt(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method sqrt of type object at 0x7106e20699e0>(*(1024,), **{}):
sqrt(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, A, J, B, P, mask):
        qk = ((A @ J) + B)
        qk = (qk / torch.sqrt(qk.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ P)
        return output




func = Model().to('cuda')



A = torch.randn(1, 64, 56, 56)



J = torch.randn(1, 64, 56, 56)



B = torch.randn(1, 64, 56, 56)



P = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))


test_inputs = [A, J, B, P, mask]

# JIT_FAIL
'''
direct:
sqrt(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method sqrt of type object at 0x767436c699e0>(*(56,), **{}):
sqrt(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
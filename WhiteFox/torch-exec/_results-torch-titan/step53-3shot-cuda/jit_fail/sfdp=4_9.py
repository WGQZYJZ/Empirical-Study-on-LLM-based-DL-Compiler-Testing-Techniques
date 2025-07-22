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

    def forward(self, Q, V7, V6, K6, V76, V1, K8, K7, V17, mask):
        qk = ((Q @ K8.transpose((- 2), (- 1))) / math.sqrt(Q.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ K6)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)



K = torch.randn(1, 64, 56, 56)



V = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))

V7 = 1
V6 = 1
K6 = 1
V76 = 1
V1 = 1
K8 = 1

test_inputs = [Q, K, V, mask, V7, V6, K6, V76, V1, K8]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
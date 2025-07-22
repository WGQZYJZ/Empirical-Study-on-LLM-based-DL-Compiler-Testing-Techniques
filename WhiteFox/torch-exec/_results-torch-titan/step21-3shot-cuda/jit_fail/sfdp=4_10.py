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
        self.w = torch.nn.Linear(32, 512)

    def forward(self, x1, x2):
        v1 = self.w(x1)
        v1 = v1.transpose((- 2), (- 1))
        v2 = self.w(x2)
        v2 = v2.transpose((- 2), (- 1))
        v3 = ((v1 @ v2) / (v1.size((- 1)) ** 0.5))
        attn_weight = torch.ones_like(v3)
        attn_weight[15:, (- 3):] = 0
        v4 = (attn_weight @ v3).transpose((- 2), (- 1))
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 16, 32)



x2 = torch.randn(1, 16, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 512].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 512, 16)), FakeTensor(..., device='cuda:0', size=(1, 512, 16))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 512].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
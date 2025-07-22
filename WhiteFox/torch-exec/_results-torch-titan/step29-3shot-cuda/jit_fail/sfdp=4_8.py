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

    def forward(self, q, k, v2, mask):
        q = q.unsqueeze((- 1))
        k = k.unsqueeze((- 3))
        v2 = v2.unsqueeze((- 3))
        qk = (q @ k.transpose((- 2), (- 1)))
        qk = (qk / math.sqrt(32))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v2)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 32)



K = torch.randn(1, 64, 32)



V = torch.randn(1, 64, 32)



mask = (torch.rand(1, 32) > 0.7).fill_((- 1000000000.0))


test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [64, 1] but got: [64, 32].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 32, 1)), FakeTensor(..., device='cuda:0', size=(1, 1, 32, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [64, 1] but got: [64, 32].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
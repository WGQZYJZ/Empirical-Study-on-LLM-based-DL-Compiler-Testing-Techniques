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

    def forward(self, q, k, v, mask):
        qk = ((q @ K.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)



K = torch.randn(1, 64, 56, 56)



V = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))


test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 56, 56)), FakeTensor(..., size=(1, 64, 56, 56))), **{}):
Unhandled FakeTensor Device Propagation for aten.bmm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
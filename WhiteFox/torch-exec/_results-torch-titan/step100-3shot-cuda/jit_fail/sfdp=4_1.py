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

    def forward(self, Q7, K7, k1, v1, mask):
        qk = ((Q7 @ K7.transpose((- 2), (- 1))) / math.sqrt(Q7.size((- 1))))
        qk = (qk + k1)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v1)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)



K = torch.randn(1, 64, 56, 56)



V = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))

Q7 = 1

test_inputs = [Q, K, V, mask, Q7]

# JIT_FAIL
'''
direct:
"baddbmm_cuda" not implemented for 'Bool'

jit:
backend='inductor' raised:
RuntimeError: Only Tensors of floating point and complex dtype can require gradients


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
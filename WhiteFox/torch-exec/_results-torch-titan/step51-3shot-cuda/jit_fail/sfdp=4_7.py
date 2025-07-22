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

    def forward(self, mask, Q, k, V):
        qk = ((Q @ k.transpose((- 2), (- 1))) / math.sqrt(Q.size((- 1))))
        qk_mask = (qk + mask)
        attn_weight = torch.softmax(qk_mask, dim=(- 1))
        output = (attn_weight @ V)
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
"baddbmm_cuda" not implemented for 'Bool'

jit:
backend='inductor' raised:
RuntimeError: Only Tensors of floating point and complex dtype can require gradients


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
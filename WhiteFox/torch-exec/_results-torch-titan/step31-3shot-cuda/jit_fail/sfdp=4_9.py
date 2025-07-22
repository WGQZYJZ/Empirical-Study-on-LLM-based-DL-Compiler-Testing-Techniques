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



class ModelWithCustomMethod(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(64, 56)

    def my_custom_linear_op(self, x):
        y = self.layer1(x)
        return (y + 10)

    def forward(self, q, k, v4, mask):
        q = self.my_custom_linear_op(q)
        k = self.my_custom_linear_op(k)
        v = self.my_custom_linear_op(v4)
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v4)
        return output




func = ModelWithCustomMethod().to('cuda')



Q = torch.randn(1, 64)



K = torch.randn(1, 64)



V = torch.randn(1, 64)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))


test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (56x56 and 1x64)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 56, 56)), FakeTensor(..., device='cuda:0', size=(1, 64))), **{}):
a and b must have same reduction dim, but got [56, 56] X [1, 64].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
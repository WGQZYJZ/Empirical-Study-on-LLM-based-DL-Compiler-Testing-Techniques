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
        self.linear1 = torch.nn.Linear(15, 1)
        self.linear2 = torch.nn.Linear(15, 5)

    def forward(self, k, v, n, q):
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        qk = qk.masked_fill((n == 1), float('-inf'))
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v)
        return output



func = Model().to('cuda')



k = torch.randn(3, 4, 5)



v = torch.randn(3, 4, 10)



n = torch.ones(3, 4)



qk = torch.randn(3, 3, 10)


test_inputs = [k, v, n, qk]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 10] but got: [3, 5].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(3, 3, 10)), FakeTensor(..., device='cuda:0', size=(3, 5, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 10] but got: [3, 5].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
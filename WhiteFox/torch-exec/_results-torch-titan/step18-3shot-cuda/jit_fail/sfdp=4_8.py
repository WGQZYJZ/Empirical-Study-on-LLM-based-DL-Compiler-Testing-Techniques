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
        self.wq = torch.nn.Linear(25, 25)
        self.wk = torch.nn.Linear(25, 25)
        self.qw = torch.nn.Parameter(torch.zeros(1, 1, 25))
        self.kw = torch.nn.Parameter(torch.zeros(1, 1, 25))

    def forward(self, q, k, v, attn_mask):
        q = self.wq(q)
        k = self.wk(k)
        qw = torch.matmul(self.qw, q.unsqueeze(2)).squeeze(2)
        kw = torch.matmul(self.kw, k.unsqueeze(2)).squeeze(2)
        qk = (torch.div(qw, 25) @ torch.div(kw, 25).T)
        qk = (qk + attn_mask)
        attn_weight = F.softmax(qk, 1)
        v = self.wv(v)
        output = torch.matmul(attn_weight, v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 5, 25)



k = torch.randn(1, 5, 25)



v = torch.randn(1, 5, 25)

attn_mask = 1

test_inputs = [q, k, v, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [5, 25] but got: [5, 1].

jit:
Failed running call_function <built-in method matmul of type object at 0x78f796a699e0>(*(Parameter(FakeTensor(..., device='cuda:0', size=(1, 1, 25), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(1, 5, 1, 25))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [5, 25] but got: [5, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.query = Parameter(torch.randn(2, 3, 5))
        self.key = Parameter(torch.randn(2, 5, 7))
        self.value = Parameter(torch.randn(2, 3, 7))
        self.dropout_p = 0.5

    def forward(self, x1):
        qk = ((self.query @ self.key.transpose((- 2), (- 1))) / math.sqrt(self.query.size((- 1))))
        qk = (qk + x1)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, self.dropout_p, True)
        return (attn_weight @ self.value)



func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 7].

jit:
Failed running call_function <built-in function matmul>(*(Parameter(FakeTensor(..., device='cuda:0', size=(2, 3, 5), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(2, 7, 5), requires_grad=True)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 7].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
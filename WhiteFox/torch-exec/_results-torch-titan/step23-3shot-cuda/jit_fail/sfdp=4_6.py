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
        self.query = torch.nn.Parameter(torch.randn(8, 1, 7, 1))

    def forward(self, x2):
        v7 = (self.query.matmul(x2).squeeze((- 1)) / math.sqrt(7))
        v8 = (v7 + 1)
        v9 = F.softmax(v8, dim=(- 1))
        v10 = x2.matmul(v9.unsqueeze((- 1))).squeeze((- 1))
        return v10



func = Model().to('cuda')



x2 = torch.randn(8, 1, 7, 1)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 1] but got: [8, 7].

jit:
Failed running call_method matmul(*(Parameter(FakeTensor(..., device='cuda:0', size=(8, 1, 7, 1), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(8, 1, 7, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 1] but got: [8, 7].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
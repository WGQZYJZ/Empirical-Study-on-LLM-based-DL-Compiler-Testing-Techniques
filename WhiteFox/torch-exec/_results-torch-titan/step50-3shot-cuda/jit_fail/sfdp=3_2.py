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

    def softmax_for_matmul(self, x1):
        v1 = torch.matmul(x1, x1.transpose((- 2), (- 1)))
        v2 = v1.mul(0.5)
        return v2.softmax(dim=(- 1))

    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, x1, x2):
        v1 = self.softmax_for_matmul(x1)
        v2 = self.dropout(v1)
        return v2.matmul(x2)



func = Model().to('cuda')



x1 = torch.randn(2, 4, 5)



x2 = torch.randn(2, 5, 6)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 5].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(2, 4, 4)), FakeTensor(..., device='cuda:0', size=(2, 5, 6))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 5].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
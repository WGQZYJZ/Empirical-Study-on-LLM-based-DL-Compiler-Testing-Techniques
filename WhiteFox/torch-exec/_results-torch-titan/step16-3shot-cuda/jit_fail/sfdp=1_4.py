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
        self.dropout_p = 0.1

    def forward(self, x1, x2):
        v1 = x1.matmul(x2.transpose((- 2), (- 1)))
        scale = (1 / math.sqrt(v1.size((- 1))))
        v2 = (v1 * scale)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=self.dropout_p)
        return x2.matmul(v4)



func = Model().to('cuda')



x1 = torch.randn(1, 64, 512)



x2 = torch.randn(1, 512, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 512] but got: [1, 64].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 64, 512)), FakeTensor(..., device='cuda:0', size=(1, 64, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 512] but got: [1, 64].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
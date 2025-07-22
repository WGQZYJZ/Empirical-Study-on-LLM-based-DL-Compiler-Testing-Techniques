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

    def forward(self, x1, x2, x3):
        v1 = (x1 @ x2.transpose((- 2), (- 1)))
        v1 = (v1 / math.sqrt(v1.size((- 1))))
        v1 = (v1 + x3)
        v2 = torch.softmax(v1, dim=(- 1))
        v3 = (v2 @ x3)
        return v3



func = Model().to('cuda')



x1 = torch.randn(2, 3, 8)



x2 = torch.randn(2, 8, 4)



x3 = torch.randn(2, 4, 7)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 8] but got: [2, 4].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 8)), FakeTensor(..., device='cuda:0', size=(2, 4, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 8] but got: [2, 4].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
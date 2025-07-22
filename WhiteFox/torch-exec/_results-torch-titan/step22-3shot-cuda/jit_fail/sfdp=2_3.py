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

    def forward(self, x1, x2):
        q1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scale_factor = (1.0 / math.sqrt(q1.shape[(- 1)]))
        v2 = q1.div(scale_factor)
        v3 = torch.exp(v2)
        v4 = torch.nn.functional.dropout(v3, 0.40395)
        v5 = torch.matmul(v4, x2)
        return v5



func = Model().to('cuda')



x1 = torch.randn(5, 7, 11)



x2 = torch.randn(8, 11, 20)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (8) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x775e288699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 7, 11)), FakeTensor(..., device='cuda:0', size=(8, 20, 11))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
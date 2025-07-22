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
        self.scale_factor = (1.0 / math.sqrt(512))
        self.dropout = torch.nn.Dropout(p=0.1)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = (v1 * self.scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = self.dropout(v3)
        return v4.matmul(x2)



func = Model().to('cuda')



x1 = torch.randn(512, 128, 512)



x2 = torch.randn(512, 512, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [512, 512] but got: [512, 128].

jit:
Failed running call_function <built-in method matmul of type object at 0x789e7e8699e0>(*(FakeTensor(..., device='cuda:0', size=(512, 128, 512)), FakeTensor(..., device='cuda:0', size=(512, 128, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [512, 512] but got: [512, 128].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
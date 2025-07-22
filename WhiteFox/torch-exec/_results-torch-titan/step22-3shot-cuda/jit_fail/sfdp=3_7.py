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
        self.w1 = torch.rand(384, 27, 2)
        self.w2 = torch.rand(128, 2, 384)

    def forward(self, x1):
        v1 = torch.matmul(self.w1, x1)
        v2 = torch.matmul(v1, self.w2)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 27, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [384, 2] but got: [384, 27].

jit:
Failed running call_function <built-in method matmul of type object at 0x794dac8699e0>(*(FakeTensor(..., device='cuda:0', size=(384, 27, 2)), FakeTensor(..., device='cuda:0', size=(1, 27, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [384, 2] but got: [384, 27].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
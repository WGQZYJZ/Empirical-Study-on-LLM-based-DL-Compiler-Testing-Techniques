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
        self.linear = torch.nn.Linear(128, 64)

    def forward(self, x1):
        return (self.linear(x1) + x1)




func = Model().to('cuda')



x1 = torch.randn(64, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (128) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(64, 64)), FakeTensor(..., device='cuda:0', size=(64, 128))), **{}):
Attempting to broadcast a dimension of length 128 at -1! Mismatching argument at index 1 had torch.Size([64, 128]); but expected shape should be broadcastable to [64, 64]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
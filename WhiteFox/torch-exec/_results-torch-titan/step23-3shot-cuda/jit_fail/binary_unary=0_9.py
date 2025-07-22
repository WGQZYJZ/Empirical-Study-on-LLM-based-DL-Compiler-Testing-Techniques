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
        self.dense1 = torch.nn.Linear(10, 16)
        self.dense2 = torch.nn.Linear(16, 5)
        self.dense3 = torch.nn.Linear(5, 256)
        self.dense4 = torch.nn.Linear(256, 1024)

    def forward(self, x1, x2):
        v1 = torch.sigmoid(self.dense1(x1))
        v2 = (v1 + x1)
        v3 = self.dense2(v2)
        v4 = (v3 + self.dense3(x2))
        v5 = torch.sin(v4)
        return self.dense4(v5)




func = Model().to('cuda')



x1 = torch.randn(1, 10)



x2 = torch.randn(1, 256)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (10) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16)), FakeTensor(..., device='cuda:0', size=(1, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([1, 10]); but expected shape should be broadcastable to [1, 16]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
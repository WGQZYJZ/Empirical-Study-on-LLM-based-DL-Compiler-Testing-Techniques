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

    def __init__(self, size):
        super().__init__()
        self.fc = torch.nn.Linear(size, 10)

    def forward(self, x1):
        t1 = self.fc(x1)
        t2 = (t1 + x1)
        t3 = F.relu(t2)
        return t3



size = 1
func = Model((28 * 28)).to('cuda')



x1 = torch.randn(16, (28 * 28))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (784) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(16, 10)), FakeTensor(..., device='cuda:0', size=(16, 784))), **{}):
Attempting to broadcast a dimension of length 784 at -1! Mismatching argument at index 1 had torch.Size([16, 784]); but expected shape should be broadcastable to [16, 10]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
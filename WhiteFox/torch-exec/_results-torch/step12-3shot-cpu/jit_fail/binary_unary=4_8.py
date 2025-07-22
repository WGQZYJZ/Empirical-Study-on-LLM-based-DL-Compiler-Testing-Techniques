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
        self.linear = torch.nn.Linear(10, 4)

    def forward(self, x2, other=None):
        v1 = self.linear(x2)
        if other is not None:
            v1 += other.squeeze()
        v2 = torch.nn.functional.relu(v1, inplace=False)
        return v2


func = Model().to('cpu')


x_tensor1 = torch.randn(1, 10)

x_tensor2 = torch.randn(1, 10)

test_inputs = [x_tensor1, x_tensor2]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (10) at non-singleton dimension 1

jit:
Failed running call_function <built-in function iadd>(*(FakeTensor(..., size=(1, 4)), FakeTensor(..., size=(s1,))), **{}):
Attempting to broadcast a dimension of length s1 at -1! Mismatching argument at index 1 had torch.Size([s1]); but expected shape should be broadcastable to [1, 4]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
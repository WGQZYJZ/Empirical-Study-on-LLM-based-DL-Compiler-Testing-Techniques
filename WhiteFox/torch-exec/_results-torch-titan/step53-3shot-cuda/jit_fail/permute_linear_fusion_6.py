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
        self.conv1d_1 = torch.nn.Conv1d(5, 10, (4,), (2,))
        self.softsign_1 = torch.nn.Softsign()

    def forward(self, x1):
        x2 = self.conv1d_1(x1)
        x3 = self.softsign_1(x2)
        x4 = (x1 * x3)
        return x4




func = Model().to('cuda')



x1 = torch.randn(1, 5, 500)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (500) must match the size of tensor b (249) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 500)), FakeTensor(..., device='cuda:0', size=(1, 10, 249))), **{}):
Attempting to broadcast a dimension of length 249 at -1! Mismatching argument at index 1 had torch.Size([1, 10, 249]); but expected shape should be broadcastable to [1, 5, 500]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        super(Model, self).__init__()
        self.dropout = torch.nn.Dropout(0.0)

    def forward(self, data_0):
        t1 = self.dropout(data_0)
        z1 = torch.flatten(t1, start_dim=1, end_dim=(- 1))
        t2 = self.dropout(data_0)
        y1 = (z1 + t2)
        return y1




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 4)), FakeTensor(..., device='cuda:0', size=(1, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 2, 2]); but expected shape should be broadcastable to [1, 1, 4]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv1d(3, 3, 3)

    def forward(self, x):
        x = self.conv(x)
        y = self.conv((x * 2))
        return (x * y).relu()




func = Model().to('cuda')



x = torch.randn(1, 3, 8)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (4) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 6)), FakeTensor(..., device='cuda:0', size=(1, 3, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 4]); but expected shape should be broadcastable to [1, 3, 6]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
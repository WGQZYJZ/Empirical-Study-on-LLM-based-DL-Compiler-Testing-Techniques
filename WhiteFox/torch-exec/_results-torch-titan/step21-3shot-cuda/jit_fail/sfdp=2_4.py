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
        qk = (x1 * x2).sum((- 1)).softmax(dim=(- 1))
        output = qk.matmul(x2)
        return output



func = Model().to('cuda')



x1 = torch.randn(2, 48)



x2 = torch.randn(65, 48)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (65) at non-singleton dimension 0

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(2, 48)), FakeTensor(..., device='cuda:0', size=(65, 48))), **{}):
Attempting to broadcast a dimension of length 65 at -2! Mismatching argument at index 1 had torch.Size([65, 48]); but expected shape should be broadcastable to [2, 48]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
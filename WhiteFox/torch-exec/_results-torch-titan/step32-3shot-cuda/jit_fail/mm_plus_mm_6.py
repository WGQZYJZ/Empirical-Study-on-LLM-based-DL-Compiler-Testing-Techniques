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

    def forward(self, input):
        t1 = torch.mm(input, input)
        t2 = (t1 * 1.1)
        t3 = t2.view(1, (- 1))
        t4 = (t3 - t2)
        t5 = t4.view((- 1))
        return t5.sum()




func = Model().to('cuda')



input = torch.randn(50, 50)


test_inputs = [input]

# JIT_FAIL
'''
direct:
The size of tensor a (2500) must match the size of tensor b (50) at non-singleton dimension 1

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 2500)), FakeTensor(..., device='cuda:0', size=(50, 50))), **{}):
Attempting to broadcast a dimension of length 50 at -1! Mismatching argument at index 1 had torch.Size([50, 50]); but expected shape should be broadcastable to [1, 2500]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
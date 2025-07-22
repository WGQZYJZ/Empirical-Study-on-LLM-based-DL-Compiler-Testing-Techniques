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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        t1 = (v1 + inp)
        t2 = torch.sigmoid(t1)
        t3 = (t2 * x1)
        t4 = t3[0:3, 2]
        t5 = t4.unsqueeze(1)
        t6 = t2[:4, :]
        return (t5, t6)




func = Model().to('cuda')



x1 = torch.randn(3, 4)



x2 = torch.randn(4, 8)



inp = torch.randn(3, 3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 8)), FakeTensor(..., device='cuda:0', size=(3, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([3, 3]); but expected shape should be broadcastable to [3, 8]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
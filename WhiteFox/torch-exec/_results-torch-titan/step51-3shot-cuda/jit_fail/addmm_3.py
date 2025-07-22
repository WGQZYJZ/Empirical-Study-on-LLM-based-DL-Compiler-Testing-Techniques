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

    def forward(self, x1, inp):
        v1 = torch.mm(x1, x1)
        v2 = v1.add_(inp)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3)



inp = torch.randn(3, 3, 3)


test_inputs = [x1, inp]

# JIT_FAIL
'''
direct:
output with shape [3, 3] doesn't match the broadcast shape [3, 3, 3]

jit:
Failed running call_method add_(*(FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(3, 3, 3))), **{}):
output with shape torch.Size([3, 3]) doesn't match the broadcast shape (3, 3, 3)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
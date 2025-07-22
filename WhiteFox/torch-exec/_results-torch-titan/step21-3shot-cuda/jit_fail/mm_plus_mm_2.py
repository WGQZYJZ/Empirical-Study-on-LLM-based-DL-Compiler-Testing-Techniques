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

    def forward(self, input1, input2, input3):
        t = torch.reshape(input3, (56, 2, 3, 4))
        t = t.transpose(1, 0)
        t = torch.reshape(t, (96, 12))
        return torch.mm(t, input2)




func = Model().to('cuda')



input1 = torch.randn(16, 16)



input2 = torch.randn(16, 16)



input3 = torch.randn(56, 8)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
shape '[56, 2, 3, 4]' is invalid for input of size 448

jit:
Failed running call_function <built-in method reshape of type object at 0x7670910699e0>(*(FakeTensor(..., device='cuda:0', size=(56, 8)), (56, 2, 3, 4)), **{}):
shape '[56, 2, 3, 4]' is invalid for input of size 448

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
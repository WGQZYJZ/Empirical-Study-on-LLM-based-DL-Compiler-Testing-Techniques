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

    def forward(self, in1, bn1, in2, bn2, in3, bn3, in4, bn4):
        t1 = torch.cat((bn1, bn2), dim=1)
        t = (torch.mm(t1, t1.transpose(0, 1)) + bn3)
        return t.mm(bn4)




func = Model().to('cuda')



in1 = torch.randn(4, 4, 4)



in2 = torch.randn(4, 4, 3)



in3 = torch.randn(3, 1)



in4 = torch.randn(4, 4)

bn1 = 1
bn2 = 1
bn3 = 1
bn4 = 1

test_inputs = [in1, in2, in3, in4, bn1, bn2, bn3, bn4]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 2

jit:
Failed running call_function <built-in method mm of type object at 0x7f829f4699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 8, 3)), FakeTensor(..., device='cuda:0', size=(8, 4, 3))), **{}):
a must be 2D

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
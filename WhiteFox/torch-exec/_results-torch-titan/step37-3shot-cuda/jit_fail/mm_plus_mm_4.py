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

    def forward(self, tensorList, tensor2):
        t1 = torch.matmul(tensorList[1], tensorList[2])
        t2 = torch.matmul(tensorList[3], tensorList[4])
        t3 = torch.matmul(tensorList[5], tensorList[7])
        t4 = torch.matmul(tensorList[6], tensor2)
        t5 = (t1 + t2)
        t6 = (t3 + t4)
        t7 = (t5 + t6)
        return t7




func = Model().to('cuda')



tensor2 = torch.randn(20, 20)

tensorList = 1

test_inputs = [tensor2, tensorList]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 2) must be Tensor, not int

jit:
Failed running call_function <built-in method matmul of type object at 0x767efd0699e0>(*(FakeTensor(..., device='cuda:0', size=(20,)), 1), **{}):
matmul(): argument 'other' (position 2) must be Tensor, not int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
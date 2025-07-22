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

    def forward(self, input1, input2):
        input3 = torch.randperm(9)
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input2)
        t3 = torch.mm(input1, input3)
        t4 = torch.mm(input2, input3)
        t5 = t1 + t2 + t3 + t4
        return t5



func = Model().to('cuda')


input1 = torch.randn(8, 8)

input2 = torch.randn(8, 8)

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method mm of type object at 0x7d0a12996ec0>(*(FakeTensor(..., size=(9,), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(s0, s1))), **{}):
a must be 2D

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
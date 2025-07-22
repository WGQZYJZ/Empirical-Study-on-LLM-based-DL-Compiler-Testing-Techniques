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

    def forward(self, input1, input2, input3, input4, input5):
        t1 = torch.mm(input1, input4)
        t2 = torch.mm(input2, input3)
        t3 = (t1 + t2)
        t4 = torch.mm(input1, input2)
        t5 = torch.mm(input3, input4)
        t6 = torch.mm(input4, input5)
        t7 = (((t4 + t5) + t6) + t3)
        return t7




func = Model().to('cuda')

input1 = 1
input2 = 1
input3 = 1
input4 = 1
input5 = 1

test_inputs = [input1, input2, input3, input4, input5]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method mm of type object at 0x71485c8699e0>(*(1, 1), **{}):
mm(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
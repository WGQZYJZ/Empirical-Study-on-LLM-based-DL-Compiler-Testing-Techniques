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

    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input3, input4)
        t2 = torch.mm(input1, input4)
        t3 = (t1 + t2)
        return t3




func = Model().to('cuda')



t1 = torch.randn(10, 5, 5)



t2 = torch.randn(5, 10, 10)

input1 = 1
input2 = 1

test_inputs = [t1, t2, input1, input2]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method mm of type object at 0x7670910699e0>(*(1, 1), **{}):
mm(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input2, input1)
        return (t1 + t2)




func = Model().to('cuda')



input = torch.randn(3, 10)

input1 = 1

test_inputs = [input, input1]

# JIT_FAIL
'''
direct:
mm(): argument 'mat2' (position 2) must be Tensor, not int

jit:
Failed running call_function <built-in method mm of type object at 0x7480ada699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 10)), 1), **{}):
mm(): argument 'mat2' (position 2) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
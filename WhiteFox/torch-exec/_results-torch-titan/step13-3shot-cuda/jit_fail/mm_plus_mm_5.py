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
        t1 = torch.mm(input2, input2)
        t2 = torch.mv(input1, input1)
        t3 = (t1 + t2)
        return t3




func = Model().to('cuda')



input1 = torch.randn(4, 4)



input2 = torch.randn(4, 4)


test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
vector + matrix @ vector expected, got 1, 2, 2

jit:
Failed running call_function <built-in method mv of type object at 0x78253ae699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4))), **{}):
matrix @ vector expected, got 2, 2

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
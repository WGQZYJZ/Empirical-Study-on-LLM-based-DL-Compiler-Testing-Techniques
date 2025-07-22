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



class Model(nn.Module):

    def forward(self, input):
        t1 = torch.mm(input)
        t2 = torch.mm(input)
        t3 = torch.mm(torch.cat([t1, t2]))
        t4 = torch.mm(torch.cat([t1, torch.mm(t1, t2)]), t3)
        return torch.mm(t3, t4)




func = Model().to('cuda')



input = torch.randn(55, 55)


test_inputs = [input]

# JIT_FAIL
'''
direct:
mm() missing 1 required positional arguments: "mat2"

jit:
Failed running call_function <built-in method mm of type object at 0x7317680699e0>(*(FakeTensor(..., device='cuda:0', size=(55, 55)),), **{}):
mm() missing 1 required positional arguments: "mat2"

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
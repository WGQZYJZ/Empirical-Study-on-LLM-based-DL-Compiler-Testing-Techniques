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
        t1 = (torch.mv(input1, input2) / input3)
        return input2.mv(input3.mv(t1))




func = Model().to('cuda')



input1 = torch.randn(5, 5)



input2 = torch.randn(5, 5)



input3 = torch.randn(5, 5)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
vector + matrix @ vector expected, got 1, 2, 2

jit:
Failed running call_function <built-in method mv of type object at 0x7f829f4699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 5)), FakeTensor(..., device='cuda:0', size=(5, 5))), **{}):
matrix @ vector expected, got 2, 2

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
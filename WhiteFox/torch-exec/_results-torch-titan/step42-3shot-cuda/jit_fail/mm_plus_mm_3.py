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

    def forward(self, input1, input2):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input2, input1)
        return torch.sigmoid(((0.3 * t1) + (0.5 * t2)))




func = Model().to('cuda')



input1 = torch.randn(3, 5)



input2 = torch.randn(5, 3)


test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (5) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(5, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([5, 5]); but expected shape should be broadcastable to [3, 3]

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
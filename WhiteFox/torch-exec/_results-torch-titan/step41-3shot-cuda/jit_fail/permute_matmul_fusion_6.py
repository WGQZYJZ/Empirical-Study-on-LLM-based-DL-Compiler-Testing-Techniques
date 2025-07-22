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

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        x1 = (x1 + 2)
        x2 = (x2 - 3)
        o1 = x1.permute(2, 0, 1)
        o2 = x2.permute(2, 1, 0)
        o3 = (o2 @ o2)
        return o3.permute(2, 2, 0)




func = Model().to('cuda')



x1 = torch.zeros((2, 4, 3))



x2 = torch.zeros((5, 3, 2))


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 3].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 5)), FakeTensor(..., device='cuda:0', size=(2, 3, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
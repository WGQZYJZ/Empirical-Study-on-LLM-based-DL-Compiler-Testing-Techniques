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

    def __init__(self, num_head):
        super().__init__()
        self.num_head = num_head

    def forward(self, x1):
        x2 = torch.matmul(x1, x1)
        x3 = torch.nn.functional.dropout(x3, p=0.1)
        x5 = (x3 * x2)
        return x5



num_head = 1

func = Model(num_head).to('cuda')



x1 = torch.randn(1, 1024, 2048)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 2048] but got: [1, 1024].

jit:
Failed running call_function <built-in method matmul of type object at 0x79536ac699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1024, 2048)), FakeTensor(..., device='cuda:0', size=(1, 1024, 2048))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 2048] but got: [1, 1024].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
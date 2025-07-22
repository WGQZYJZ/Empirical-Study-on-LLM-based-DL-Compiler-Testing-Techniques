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
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2, bias=False)
        self.linear3 = torch.nn.Linear(2, 2, bias=False)

    def forward(self, x1):
        x2 = x1.permute(0, 2, 1)
        x3 = torch.nn.functional.linear(x2, self.linear1.weight, output_process_bias=None)
        x4 = torch.nn.functional.linear(x2, self.linear2.weight, None)
        x5 = torch.maximum(x4, x3)
        x6 = x5.permute(0, 2, 1)
        x7 = torch.nn.functional.linear(x6, self.linear3.weight, None)
        return x7




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear() got an unexpected keyword argument 'output_process_bias'

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(2, 2), requires_grad=True))), **{'output_process_bias': None}):
linear() got an unexpected keyword argument 'output_process_bias'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.fc1 = torch.nn.Linear(3, 3)

    def forward(self, input_tensor):
        fc_result = torch.nn.functional.conv2d(input_tensor, self.fc1.weight, self.fc1.bias)
        self.bn = torch.nn.BatchNorm2d(3)
        return fc_result




func = Model().to('cuda')



input_tensor = torch.randn(1, 3, 3, 3)


test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
weight should have at least three dimensions

jit:
Failed running call_function <built-in method conv2d of type object at 0x7df0e32699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 3, 3)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(3,), requires_grad=True))), **{}):
expected stride to be a single integer value or a list of 0 values to match the convolution dimensions, but got stride=[1, 1]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
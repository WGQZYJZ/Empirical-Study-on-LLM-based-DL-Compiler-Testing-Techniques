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

    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(20, 20)
        self.fc2 = nn.Linear(20, 20)
        self.fc3 = nn.Linear(20, 20)
        self.fc4 = nn.Linear(20, 20)

    def forward(self, input1, input2, input3, input4):
        output = self.fc1(input1)
        output = self.fc2(input2)
        output = self.fc3(input3)
        output = self.fc4(input4)
        return output.mm(output.mm(output))



func = Model().to('cpu')


input1 = torch.randn(20, 5)

input2 = torch.randn(20, 5)

input3 = torch.randn(20, 5)

input4 = torch.randn(20, 5)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x5 and 20x20)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(20, 5)), Parameter(FakeTensor(..., size=(20, 20), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [20, 5] X [20, 20].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
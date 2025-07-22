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

class ModelFactory:

    @staticmethod
    def build_model():
        return torch.nn.Sequential(torch.nn.Linear(3, 64), torch.nn.Linear(64, 128))

class MyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.model_factory = ModelFactory()

    def forward(self, x1):
        return self.model_factory.build_model()(x1)


func = MyModel().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x64 and 3x64)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 3, 64, 64)), Parameter(FakeTensor(..., size=(64, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [192, 64] X [3, 64].

from user code:
   File "<string>", line 26, in torch_dynamo_resume_in_forward_at_26
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
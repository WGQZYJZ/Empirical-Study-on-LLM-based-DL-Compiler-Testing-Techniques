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

class Module1(torch.nn.Module):

    def __init__(self, batchnorm2d):
        super().__init__()
        if batchnorm2d:
            self.op1 = torch.nn.Sequential(torch.nn.BatchNorm2d(16), torch.nn.ReLU(inplace=False), torch.nn.Conv2d(16, 16, 1, 1, 0))
        else:
            self.op1 = torch.nn.Sequential(torch.nn.ReLU(inplace=False), torch.nn.Conv2d(16, 16, 1, 1, 0))

    def forward(self, x):
        return self.op1(x)

class Module2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.op2 = torch.nn.Sequential(torch.nn.BatchNorm2d(16), torch.nn.ReLU(inplace=False), torch.nn.Conv2d(16, 16, 1, 1, 0))

    def forward(self, x):
        return self.op2(x)

class Module3(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.op3 = torch.nn.Sequential(torch.nn.ReLU(inplace=False), torch.nn.Conv2d(16, 16, 1, 1, 0))
        self.op4 = torch.nn.Sequential(torch.nn.BatchNorm2d(16), torch.nn.ReLU(inplace=False), torch.nn.Conv2d(16, 16, 1, 1, 0))

    def forward(self, x):
        x = self.op3(x)
        return self.op4(x)

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.features = torch.nn.Sequential(Module1(batchnorm2d=False), torch.nn.Conv2d(16, 16, 1, 1, 0), Module2(), Module3(), torch.nn.BatchNorm2d(16))

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 32, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 32 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x727fda97bf70>(*(FakeTensor(..., size=(1, 32, 64, 64)), [1, 1, 1]), **{'dim': 1}):
Split sizes add up to 3 but got the tensor's size of 32

from user code:
   File "<string>", line 52, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
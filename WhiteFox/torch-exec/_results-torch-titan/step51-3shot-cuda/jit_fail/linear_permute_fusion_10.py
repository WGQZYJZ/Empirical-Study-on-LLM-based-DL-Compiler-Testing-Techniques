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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        yuzu.onnxrt.set_training(1)
        v2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v3 = v2.permute(0, 2, 1)
        return v3




func = Model().to('cuda')



x1 = torch.randn(4, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'yuzu' is not defined

jit:
name 'yuzu' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
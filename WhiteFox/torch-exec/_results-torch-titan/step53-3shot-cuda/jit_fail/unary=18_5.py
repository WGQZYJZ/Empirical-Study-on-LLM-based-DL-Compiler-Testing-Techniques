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
        self.v2 = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=1, stride=1, padding=0)
        self.v3 = torch.nn.Sigmoid()
        self.v4 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.v5 = torch.nn.Sigmoid()
        self.v6 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.v7 = torch.nn.Sigmoid()
        self.v8 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.v10 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.v11 = torch.nn.Sigmoid()
        self.v12 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.v14 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.v15 = torch.nn.Sigmoid()
        self.v16 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.v2(x1)
        v2 = self.v3(v1)
        v3 = self.v4(v2)
        v4 = self.v5(v3)
        v5 = self.v6(v4)
        v6 = self.v7(v5)
        v7 = self.v8(v6)
        v8 = self.v10(v6)
        v9 = (v8 + v7)
        v10 = self.v11(v9)
        v11 = self.v12(v10)
        v12 = (v9 + v11)
        v13 = self.v14(v12)
        v14 = self.v15(v13)
        v15 = self.v16(v14)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'v16' is not defined

jit:
name 'v16' is not defined

from user code:
   File "<string>", line 49, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
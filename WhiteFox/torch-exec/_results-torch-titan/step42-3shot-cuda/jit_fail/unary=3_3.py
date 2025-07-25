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
        self.conv = torch.nn.Conv2d(3, 13, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(26, 19, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(26, 14, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(13, 20, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(13, 15, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(14, 18, 1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(26, 34, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = (v7 * 0.5)
        v9 = (v7 * 0.7071067811865476)
        v10 = torch.erf(v9)
        v11 = (v10 + 1)
        v12 = (v8 * v11)
        v13 = self.conv3(v12)
        v14 = (v7 * 0.5)
        v15 = (v7 * 0.7071067811865476)
        v16 = torch.erf(v15)
        v17 = (v16 + 1)
        v18 = (v14 * v17)
        v19 = self.conv4(v18)
        v20 = (v13 * 0.5)
        v21 = (v13 * 0.7071067811865476)
        v22 = torch.erf(v21)
        v23 = (v22 + 1)
        v24 = (v20 * v23)
        v25 = self.conv5(v24)
        v26 = (v12 * 0.5)
        v27 = (v12 * 0.7071067811865476)
        v28 = torch.erf(v27)
        v29 = (v28 + 1)
        v30 = (v26 * v29)
        v31 = self.conv6(v30)
        v32 = (v19 * v31)
        v33 = (v12 * 0.5)
        v34 = (v12 * 0.7071067811865476)
        v35 = torch.erf(v34)
        v36 = (v35 + 1)
        v37 = (v33 * v36)
        v38 = self.conv7(v37)
        return v38




func = Model().to('cuda')



x1 = torch.randn(1, 3, 131, 131)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [19, 26, 1, 1], expected input[1, 13, 131, 131] to have 26 channels, but got 13 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 13, 131, 131)),), **{}):
Given groups=1, weight of size [19, 26, 1, 1], expected input[1, 13, 131, 131] to have 26 channels, but got 13 channels instead

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        super().__init__()
        self.conv1 = torch.nn.Conv2d(64, 96, kernel_size=3, stride=1, padding=1)
        self.conv12 = torch.nn.Conv2d(64, 96, kernel_size=3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(96, 128, kernel_size=1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(96, 128, kernel_size=1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(96, 128, kernel_size=1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(64, 192, kernel_size=3, stride=1, padding=1)
        self.conv31 = torch.nn.Conv2d(96, 192, kernel_size=3, stride=2, padding=1)
        self.conv7 = torch.nn.Conv2d(192, 256, kernel_size=1, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(192, 256, kernel_size=1, stride=1, padding=0)
        self.conv9 = torch.nn.Conv2d(192, 256, kernel_size=1, stride=1, padding=0)
        self.conv10 = torch.nn.Conv2d(128, 384, kernel_size=1, stride=1, padding=0)
        self.conv11 = torch.nn.Conv2d(192, 128, kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v2)
        v5 = self.conv5(v2)
        v6 = self.conv6(v1)
        v31 = self.conv31(v1)
        v7 = self.conv7(v1)
        v8 = self.conv8(v1)
        v9 = self.conv9(v1)
        v10 = self.conv10(v3)
        v11 = self.conv11(v1)
        v12 = self.conv12(x1)
        v13 = torch.relu((v11 + v12))
        v14 = torch.relu((v7 + v8))
        v15 = torch.relu((v9 + v10))
        v15 = torch.relu((v9 + v10))
        v16 = torch.relu((v14 + v15))
        v17 = torch.cat([v13, v6, v16], 1)
        v18 = torch.cat([v13, v31, v16], 1)
        v19 = self.conv11(v18)
        v20 = torch.relu((v17 + v19))
        return v20




func = Model().to('cuda')



x1 = torch.randn(1, 64, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv2'

jit:
conv2

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
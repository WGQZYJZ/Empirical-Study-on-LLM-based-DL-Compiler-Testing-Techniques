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
        conv0 = torch.nn.Conv2d(16, 16, [1, 9], stride=1, padding=[0, 4])
        pool0 = torch.nn.MaxPool2d(kernel_size=[1, 1], stride=[1, 4], padding=0, dilation=1, ceil_mode=False)
        self.conv1 = torch.nn.Conv2d(16, 16, [1, 15], stride=1, padding=[0, 7])
        self.add0 = torch.nn.quantized.FloatFunctional()
        conv2 = torch.nn.Conv2d(16, 16, [1, 1], stride=1, padding=[0, 0])
        mul1 = torch.nn.quantized.FloatFunctional()
        conv3 = torch.nn.Conv2d(16, 16, [1, 7], stride=1, padding=[0, 3])
        add2 = torch.nn.quantized.FloatFunctional()
        pool3 = torch.nn.MaxPool2d(kernel_size=15, stride=1, padding=0, dilation=1, ceil_mode=False)
        conv4 = torch.nn.Conv2d(16, 16, [1, 1], stride=1, padding=0)
        mul3 = torch.nn.quantized.FloatFunctional()
        conv5 = torch.nn.Conv2d(16, 16, [1, 5], stride=1, padding=[0, 2])
        add4 = torch.nn.quantized.FloatFunctional()
        conv6 = torch.nn.Conv2d(16, 16, [1, 1], stride=1, padding=0)
        mul5 = torch.nn.quantized.FloatFunctional()
        conv7 = torch.nn.Conv2d(16, 16, [1, 3], stride=1, padding=[0, 1])
        mul7 = torch.nn.quantized.FloatFunctional()
        conv8 = torch.nn.Conv2d(16, 16, [1, 1], stride=1, padding=0)
        add6 = torch.nn.quantized.FloatFunctional()
        conv9 = torch.nn.Conv2d(16, 16, [1, 5], stride=1, padding=[0, 2])
        conv10 = torch.nn.Conv2d(16, 16, [1, 5], stride=1, padding=[0, 2])
        conv11 = torch.nn.Conv2d(16, 16, [1, 5], stride=1, padding=[0, 2])
        conv12 = torch.nn.Conv2d(16, 16, [1, 5], stride=1, padding=[0, 2])

    def forward(self, x):
        v1 = self.conv0(x)
        v2 = self.pool0(v1)
        v3 = self.conv1(v2)
        v4 = self.add0.add_relu_(v3, x)
        v5 = self.conv2(v4)
        v7 = self.pool0(v5)
        v6 = self.mul1.mul_relu_(v7, v6)
        v8 = self.conv3(v6)
        v9 = self.add2.add_relu_(v8, v9)
        v10 = self.pool3(v9)
        v11 = self.conv4(v10)
        v12 = self.conv6(v11)
        v14 = self.conv4(v12)
        v13 = self.mul3.mul_relu_(v14, v13)
        v15 = self.conv5(v13)
        v16 = self.add4.add_relu_(v15, v16)
        v17 = self.conv6(v16)
        v18 = self.pool0(v17)
        v19 = self.conv6(v18)
        v21 = self.conv7(v19)
        v20 = self.mul7.mul_relu_(v21, v20)
        v22 = self.conv8(v20)
        v23 = self.add6.add_relu_(v22, v23)
        v24 = self.conv9(v23)
        v25 = self.conv7(v24)
        v26 = self.conv10(v25)
        v27 = self.conv11(v26)
        v28 = self.conv9(v27)
        v31 = self.conv12(v28)
        v30 = self.add6.add_relu_(v31, v30)
        concat1 = self.add2.cat([v13, v11, v27, v21, v14, v24, v26, v22, v30, v8], 1)
        return concat1




func = Model().to('cuda')




x = torch.randn(1, 64, 28, 28, dtype=torch.float32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv0'

jit:
conv0

from user code:
   File "<string>", line 44, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
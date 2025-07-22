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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_conv1 = torch.nn.Conv2d(8, 16, 1)
        self.other_conv2 = torch.nn.Conv2d(16, 32, 1)
        self.other_conv3 = torch.nn.Conv2d(32, 16, 1)
        self.other_conv4 = torch.nn.Conv2d(16, 8, 1)
        self.other_conv5 = torch.nn.Conv2d(8, 8, 1)
        self.other_conv6 = torch.nn.Conv2d(8, 8, 1)
        self.other_conv7 = torch.nn.Conv2d(8, 8, 1)

    def forward(self, x1):
        v1 = (3 + self.conv(x1))
        v2 = (v1 - 1)
        v3 = (v1 * 1)
        v4 = (v1 / 1)
        v5 = (1 - v4)
        v6 = (1 + v2)
        v7 = (1 * v3)
        v8 = (v7 / 1)
        v9 = v1.neg()
        v10 = v9
        v11 = (v8 * 6)
        v12 = (v6 * 6)
        v13 = (v12 - 6)
        v14 = (v13 / 6)
        v15 = (1 / v5)
        v16 = (v14 * v15)
        v17 = (v11 / 6)
        v18 = (3 + v17)
        v19 = (6 / v8)
        v20 = (6 / v6)
        v21 = torch.clamp_max(v20, 6)
        v22 = torch.clamp_min(v19, 0)
        v23 = (v21 * v22)
        v24 = (v18 * 6)
        v25 = (v24 / 6)
        v26 = (v23 * 6)
        v27 = (v25 * v26)
        v28 = (v16 * v27)
        v29 = (v3 + 3)
        v30 = (6 / v10)
        v31 = torch.clamp_min(v30, 0)
        v32 = (v31 * 6)
        v33 = (v29 * v32)
        x2 = (v28 + v33)
        v35 = (3 / x2)
        v36 = v16.div(6)
        return self.other_conv7(self.other_conv6(self.other_conv5(self.other_conv4(self.other_conv3(self.other_conv2(self.other_conv1(v35)))))))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3h_m030g/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp3h_m030g', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp3h_m030g/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
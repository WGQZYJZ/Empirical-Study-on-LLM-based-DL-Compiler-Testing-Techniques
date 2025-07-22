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
        self.conv = torch.nn.Conv2d(1, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 128, 5, stride=2, padding=2)
        self.conv3 = torch.nn.Conv2d(128, 8, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(8, 64, 3, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(64, 8, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(8, 128, 7, stride=2, padding=3)
        self.conv7 = torch.nn.Conv2d(128, 256, 1, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(256, 112, 7, stride=1, padding=3)

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
        v14 = (v13 * 0.5)
        v15 = (v13 * 0.7071067811865476)
        v16 = torch.erf(v15)
        v17 = (v16 + 1)
        v18 = (v14 * v17)
        v19 = self.conv4(v18)
        v20 = (v19 * 0.5)
        v21 = (v19 * 0.7071067811865476)
        v22 = torch.erf(v21)
        v23 = (v22 + 1)
        v24 = (v20 * v23)
        v25 = self.conv5(v24)
        v26 = (v25 * 0.5)
        v27 = (v25 * 0.7071067811865476)
        v28 = torch.erf(v27)
        v29 = (v28 + 1)
        v30 = (v26 * v29)
        v31 = self.conv6(v30)
        v32 = (v31 * 0.5)
        v33 = (v31 * 0.7071067811865476)
        v34 = torch.erf(v33)
        v35 = (v34 + 1)
        v36 = (v32 * v35)
        v37 = self.conv7(v36)
        v38 = (v37 * 0.5)
        v39 = (v37 * 0.7071067811865476)
        v40 = torch.erf(v39)
        v41 = (v40 + 1)
        v42 = (v38 * v41)
        v43 = self.conv8(v42)
        return (v43, v42)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 1024, 1024)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpy46g0y8u/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpy46g0y8u', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpy46g0y8u/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
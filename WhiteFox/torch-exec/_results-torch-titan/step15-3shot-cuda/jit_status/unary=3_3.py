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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=8)
        self.conv2 = torch.nn.Conv2d(8, 8, 5, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * 0.08288301170549509)
        v3 = (v1 * 4.391375896806684e-18)
        v4 = (v1 * 0.5)
        v5 = (v1 * 0.4999999999999991)
        v6 = (v1 * 0.4131728549995799)
        v7 = (v1 * 0.31946795909149245)
        v8 = torch.erf(v7)
        v9 = (v1 * 0.2616614722486103)
        v10 = (v1 * 0.21847764755691068)
        v11 = (v1 * 0.183218962865971)
        v12 = (v1 * 0.1536442572875255)
        v13 = torch.erf(v12)
        v14 = (v1 * 0.1300138116012838)
        v15 = (v1 * 0.10961566197062866)
        v16 = (v1 * 0.0919533908195234)
        v17 = (v1 * 0.07673879072256343)
        v18 = (v1 * 0.06343727816799351)
        v19 = (v1 * 0.05176020890542962)
        v20 = (v1 * 0.04151599014640475)
        v21 = (v1 * 0.03237205795806821)
        v22 = (v1 * 0.024950481556130114)
        v23 = (v1 * 0.018766112513845454)
        v24 = (v1 * 0.01329955056072879)
        v25 = (v1 * 0.0089676507019985)
        v26 = (v1 * 0.00548681252128987)
        v27 = (v1 * 0.002738894159601448)
        v28 = (v1 * 0.0008779654828145495)
        v29 = (v1 * 6.70267327844902e-11)
        v30 = (v1 * 2.6308929987433705e-16)
        v31 = self.conv2(v3)
        return v31




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwhiichho/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpwhiichho', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpwhiichho/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
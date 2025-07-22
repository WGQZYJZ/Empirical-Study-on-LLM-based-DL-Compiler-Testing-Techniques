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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 4, (2, 2), stride=(1, 1), padding=(0, 0), dilation=1, groups=1, bias=False)
        self.batch_norm = torch.nn.BatchNorm2d(4, momentum=0.0010000000474974513, eps=0.0009999999747378752, affine=True, track_running_stats=True)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(4, 4, (3, 3), stride=(1, 1), padding=(0, 0), dilation=1, groups=1, bias=False)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * 0.5)
        v3 = ((v1 * v1) * v1)
        v4 = (v3 * 0.044715)
        v5 = (v1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v2 * v8)
        v10 = torch.sigmoid(v9)
        v11 = (v10 + 1)
        v12 = self.batch_norm(v11)
        v13 = self.conv_transpose2(v12)
        v14 = (v13 * 0.5)
        v15 = ((v13 * v13) * v13)
        v16 = (v15 * 0.044715)
        v17 = (v13 + v16)
        v18 = (v17 * 0.7978845608028654)
        v19 = torch.tanh(v18)
        v20 = (v19 + 1)
        v21 = (v14 * v20)
        return v21




func = Model().to('cuda')



x1 = torch.randn(3, 3, 5, 5)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4u392jmo/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp4u392jmo', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp4u392jmo/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
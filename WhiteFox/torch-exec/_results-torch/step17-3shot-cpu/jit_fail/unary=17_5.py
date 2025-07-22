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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 32, 3, padding=1, stride=1)

    def forward(self, x1):
        v1 = torch.nn.functional.interpolate(x1, scale_factor=1.0, recompute_scale_factor=False)
        v2 = v1.contiguous()
        v3 = v2.float()
        v4 = v3.to(torch.float16)
        v5 = v4.to(torch.float32)
        v6 = v5.to(torch.float64)
        v7 = v6.to(torch.int8)
        v8 = v7.to(torch.int16)
        v9 = v8.to(torch.int32)
        v10 = v9.to(torch.int64)
        v11 = v10.to(torch.bool)
        v12 = v11.to(torch.complex64)
        v13 = v12.to(torch.complex128)
        v14 = v13.to(torch.qint8)
        v15 = v14.to(torch.quint8)
        v16 = v15.to(torch.qint32)
        v17 = v13.to(torch.bfloat16)
        return v17



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
empty_strided not supported on quantized tensors yet see https://github.com/pytorch/pytorch/issues/74540

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwh486aos/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwh486aos/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwh486aos', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
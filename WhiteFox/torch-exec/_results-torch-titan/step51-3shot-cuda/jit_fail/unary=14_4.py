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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(1, 8, 17, stride=4, padding=(4, 4))
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(8, 8, 12, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = nn.BatchNorm2d(8, eps=2.0)
        v3 = v2(v1)
        v4 = torch.sigmoid(v3)
        v5 = (v3 * v4)
        v6 = self.conv_transpose_2(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 1, 37, 37)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument weight in method wrapper_CUDA__cudnn_batch_norm)

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfigoegur/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpfigoegur', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpfigoegur/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
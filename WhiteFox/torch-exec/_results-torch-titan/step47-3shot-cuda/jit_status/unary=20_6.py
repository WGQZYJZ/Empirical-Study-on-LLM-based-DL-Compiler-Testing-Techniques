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
        self.conv_transpose2d = torch.nn.ConvTranspose2d(1, 512, 1, 1)
        self.conv2d = torch.nn.Conv2d(512, 1, 1, 1)

    def forward(self, x0):
        v0 = F.relu(x0)
        v1 = self.conv_transpose2d(v0)
        v10 = self.conv2d(v1)
        v3 = torch.sigmoid(v10)
        return v3




func = Model().to('cuda')



x0 = torch.randn(1, 1, 5, 5)


test_inputs = [x0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl10jxevm/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpl10jxevm', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpl10jxevm/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
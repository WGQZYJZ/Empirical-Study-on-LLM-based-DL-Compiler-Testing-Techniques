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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.tanh(self.conv1(x1))
        if (v1.size()[0] == 1):
            v2 = torch.nn.functional.conv3d(v1, input_tensor)
            v3 = torch.nn.functional.relu(v2)
            v4 = torch.nn.functional.interpolate(v3.unsqueeze(dim=0), scale_factor=2.0, mode='trilinear')
        else:
            v4 = v1
        return v4




func = Model().to('cuda')



x1 = torch.randn(3, 3, 107, 107)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpink2c1sp/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpink2c1sp', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpink2c1sp/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
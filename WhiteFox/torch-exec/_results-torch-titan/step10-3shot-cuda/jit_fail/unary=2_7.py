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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(3, 3, 2, stride=2, output_padding=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(3, 3, 1, stride=1, output_padding=1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(3, 3, 3, stride=3, padding=1, output_padding=1)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(3, 3, 3, stride=3, padding=3, output_padding=1)
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(3, 3, 3, stride=3, padding=3, output_padding=3)
        self.conv_transpose_6 = torch.nn.ConvTranspose2d(3, 3, 3, stride=3, padding=3, output_padding=3)
        self.conv_transpose_7 = torch.nn.ConvTranspose2d(3, 3, 2, stride=2, output_padding=0)
        self.conv_transpose_8 = torch.nn.ConvTranspose2d(3, 3, 2, stride=2, output_padding=0)
        self.conv_transpose_9 = torch.nn.ConvTranspose2d(3, 1, 3, stride=1, padding=0)
        self.conv_transpose_10 = torch.nn.ConvTranspose2d(3, 3, 3, stride=3, padding=1, output_padding=(1, 0))
        self.conv_transpose_11 = torch.nn.ConvTranspose2d(3, 3, 3, stride=3, padding=1, output_padding=(0, 1))
        self.conv_transpose_12 = torch.nn.ConvTranspose2d(3, 3, 3, stride=3, padding=1, output_padding=(1, 1))
        self.batch_normalization = torch.nn.BatchNorm2d(3, affine=True)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv_transpose_2(x1)
        v3 = self.conv_transpose_3(x1)
        v4 = self.conv_transpose_4(x1)
        v5 = self.conv_transpose_5(x1)
        v6 = self.conv_transpose_6(x1)
        v7 = self.conv_transpose_7(x1)
        v8 = self.conv_transpose_8(x1)
        v9 = self.conv_transpose_9(x1)
        v10 = self.conv_transpose_10(x1)
        v11 = self.conv_transpose_11(x1)
        v12 = self.conv_transpose_12(x1)
        v13 = self.batch_normalization(x1)
        return [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13]




func = Model().to('cuda')



x1 = torch.randn(1, 3, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpt0tz7aob/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpt0tz7aob', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpt0tz7aob/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
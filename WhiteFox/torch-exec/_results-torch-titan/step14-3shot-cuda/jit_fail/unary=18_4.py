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



class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.conv1_1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv1_2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv1_3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv2_1 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=2, padding=1)
        self.conv2_2 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.conv2_3 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.conv3_1 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=2, padding=1)
        self.conv3_2 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, stride=1, padding=1)
        self.conv3_3 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, stride=1, padding=1)
        self.conv4_1 = nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, stride=2, padding=1)
        self.conv4_2 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1)
        self.conv4_3 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1)
        self.conv5_1 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=2, padding=1)
        self.conv5_2 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1)
        self.conv5_3 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        conv_out = self.conv1_1(x)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv1_2(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv1_3(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv2_1(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv2_2(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv2_3(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv3_1(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv3_2(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv3_3(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv4_1(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv4_2(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv4_3(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv5_1(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv5_2(conv_out)
        conv_out = nn.ReLU(conv_out)
        conv_out = self.conv5_3(conv_out)
        conv_out = nn.ReLU(conv_out)
        return conv_out




func = Model().to('cuda')



x = torch.randn(1, 3, 224, 224)


test_inputs = [x]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (ReLU, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!ReLU!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!ReLU!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpz4d204ds/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpz4d204ds', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpz4d204ds/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
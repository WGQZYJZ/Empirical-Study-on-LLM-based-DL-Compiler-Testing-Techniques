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



class Attention(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.25)

    def forward(self, query, key, value, scale_factor=None):
        global attention_mask
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        if (scale_factor is not None):
            scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        attention_mask = softmax_qk
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



func = Attention().to('cuda')



query = torch.randn(1, 8, 64, 64)



key = torch.randn(1, 8, 64, 64)



value = torch.randn(1, 8, 64, 64)



scale_factor = torch.randn(1, 8, 1, 1)


test_inputs = [query, key, value, scale_factor]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp74g872vc/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp74g872vc', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp74g872vc/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
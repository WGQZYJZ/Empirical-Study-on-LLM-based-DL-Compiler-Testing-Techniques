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
        self.num_heads = 1
        self.head_dim = 1

    def forward(self, query, key, value, attn_mask):
        qk = (torch.matmul(query, key.transpose((- 2), (- 1))) / math.sqrt(self.head_dim))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = torch.matmul(attn_weight, value)
        return output




func = Model().to('cuda')



query = torch.randn(2, 2, 8, 16)



key = torch.randn(2, 2, 8, 16)



value = torch.randn(2, 2, 8, 16)




attn_mask = torch.logical_not(torch.eye(8)).unsqueeze(0).unsqueeze(0)


test_inputs = [query, key, value, attn_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpsq1yyfyc/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpsq1yyfyc', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpsq1yyfyc/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
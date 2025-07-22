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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, q, k, v, attention_mask):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + attention_mask
        attention_weight = torch.softmax(qk, dim=-1)
        output = attention_weight @ v
        return output


func = Model().to('cpu')

head_num = 8
d_model = 128
head_num = 8
batch_size = 1

q_seq_len = 32
q = torch.randn(batch_size * head_num, q_seq_len, d_model // head_num)
head_num = 8
d_model = 128
head_num = 8
batch_size = 1

k_seq_len = 32
k = torch.randn(batch_size * head_num, k_seq_len, d_model // head_num)
head_num = 8
d_model = 128
head_num = 8
batch_size = 1

v_seq_len = 32
v = torch.randn(batch_size * head_num, v_seq_len, d_model // head_num)
attention_mask = 1

test_inputs = [q, k, v, attention_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3jceu2to/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp3jceu2to/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp3jceu2to', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
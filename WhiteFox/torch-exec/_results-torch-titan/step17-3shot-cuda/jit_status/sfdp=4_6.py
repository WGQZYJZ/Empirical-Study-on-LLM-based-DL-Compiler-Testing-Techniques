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
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        qk = (qk + attention_mask)
        attention_weight = torch.softmax(qk, dim=(- 1))
        output = (attention_weight @ v)
        return output



func = Model().to('cuda')


head_num = 8


d_model = 128


head_num = 8


batch_size = 1



q_seq_len = 32


q = torch.randn((batch_size * head_num), q_seq_len, (d_model // head_num))


head_num = 8


d_model = 128


head_num = 8


batch_size = 1



k_seq_len = 32


k = torch.randn((batch_size * head_num), k_seq_len, (d_model // head_num))


head_num = 8


d_model = 128


head_num = 8


batch_size = 1



v_seq_len = 32


v = torch.randn((batch_size * head_num), v_seq_len, (d_model // head_num))

attention_mask = 1

test_inputs = [q, k, v, attention_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxykijo69/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpxykijo69', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpxykijo69/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
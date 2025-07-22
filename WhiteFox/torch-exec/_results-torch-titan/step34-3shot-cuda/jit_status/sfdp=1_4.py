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

    def __init__(self, batch_size, seq_len, num_head):
        super().__init__()
        self.batch_size = batch_size
        self.seq_len = seq_len
        self.num_head = num_head

    def forward(self, q, k, v):
        q = q.reshape((self.batch_size * self.seq_len), self.num_head, (- 1))
        k = k.reshape((self.batch_size * self.seq_len), self.num_head, (- 1))
        v = v.reshape((self.batch_size * self.seq_len), self.num_head, (- 1))
        q = q.permute(1, 0, 2)
        k = k.permute(1, 0, 2)
        v = v.permute(1, 0, 2)
        qk = torch.matmul(q, k.transpose(1, 2))
        scaled_qk = qk.div((64 ** 0.5))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(v)
        output = output.transpose(1, 0)
        output = output.reshape(self.num_head, self.batch_size, self.seq_len, (- 1))
        output = output.permute(1, 2, 0, 3)
        return output



batch_size = 1
seq_len = 1
num_head = 1
func = Model(1, 512, 8).to('cuda')



q = torch.randn(512, 8, 32)



k = torch.randn(512, 8, 32)



v = torch.randn(512, 8, 64)


test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpduw6rj9p/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpduw6rj9p', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpduw6rj9p/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
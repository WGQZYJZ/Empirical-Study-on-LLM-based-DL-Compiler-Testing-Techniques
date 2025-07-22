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

    def __init__(self, embed_dim, num_heads, dropout_p=0.1):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.head_dim = (embed_dim // num_heads)
        self.inv_scale_factor = (self.head_dim ** (- 0.5))
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.reshape = torch.nn.Linear(embed_dim, embed_dim)

    def forward(self, x1, x2):
        scale_factor = torch.sqrt(torch.as_tensor(self.head_dim).float())
        qk = torch.matmul(self.reshape(x1), x2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(x2)
        return output



embed_dim = 1
num_heads = 1
func = Model(2048, 16).to('cuda')



x1 = torch.randn(1, 256, 2048)



x2 = torch.randn(1, 256, 2048)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3grfkv2w/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp3grfkv2w', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp3grfkv2w/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
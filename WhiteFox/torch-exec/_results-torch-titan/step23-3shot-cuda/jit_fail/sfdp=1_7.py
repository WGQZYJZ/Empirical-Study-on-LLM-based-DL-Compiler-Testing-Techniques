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



class Conv(torch.nn.Module):

    def __init__(self, qk_depth, v_depth):
        super().__init__()
        self.depth = (max(qk_depth, v_depth) // 2)
        self.qk_depth = qk_depth
        self.v_depth = v_depth
        self.project = torch.nn.Sequential(torch.nn.Conv2d(self.qk_depth, self.depth, 1, bias=False), torch.nn.BatchNorm2d(self.depth), torch.nn.ReLU(inplace=True))
        self.conv = torch.nn.Conv2d(self.depth, self.depth, 1, bias=False)
        self.reduce = torch.nn.Sequential(torch.nn.BatchNorm2d(self.depth), torch.nn.ReLU(inplace=False), torch.nn.Conv2d(self.depth, self.v_depth, 1))
        self.unproject_v = torch.nn.Conv2d(self.depth, self.v_depth, 1, bias=False)
        self.unproject_qk = torch.nn.Conv2d(self.depth, self.qk_depth, 1, bias=False)

    def forward(self, x1, x2, mask=None, x_v_proj=None, dropout_p=0.0):
        (batch_size, _, height, width) = x1.size()
        v = (x1 + x2)
        y = self.project(v)
        if (x_v_proj is None):
            x_v_proj = self.conv(y)
        qk = x_v_proj[:, :self.qk_depth]
        v = x_v_proj[:, self.qk_depth:]
        if (dropout_p > 0.0):
            qk = (torch.nn.functional.dropout(qk, p=dropout_p) * (1 - mask.float()))
        qk = qk.reshape(batch_size, (height * width), self.qk_depth)
        qk = F.normalize(qk, p=2, dim=2)
        w = torch.matmul(qk.transpose((- 2), (- 1)), v)
        w = F.normalize(w, p=2, dim=2)
        w = w.reshape(batch_size, self.qk_depth, height, width)
        w = self.reduce(w)
        v = self.unproject_v(v)
        y = self.unproject_qk(w)
        v = (v + x2)
        if (dropout_p > 0.0):
            y = (torch.nn.functional.dropout(y, p=dropout_p) * (1 - mask.float()))
        return (v, y)




class Model(torch.nn.Module):

    def __init__(self, dropout_p):
        super().__init__()
        self.dropout_probability = dropout_p
        self.q_conv = Conv(64, 32)
        self.k_conv = Conv(64, 32)
        self.v_conv = Conv(64, 32)
        self.out_conv = Conv(64, 64)

    def forward(self, x1, x2, mask=None):
        (batch_size, channels, height, width) = x1.size()
        mask = mask.float()
        (q, y) = self.q_conv(x1, x2, mask, dropout_p=self.dropout_probability)
        (k, y) = self.k_conv(x2, x2, mask, dropout_p=self.dropout_probability)
        (v, y) = self.v_conv(x2, x2, mask, dropout_p=self.dropout_probability)
        w = torch.matmul(q.transpose((- 2), (- 1)), k)
        w = F.normalize(w, p=2, dim=3)
        w = (w / math.sqrt(channels))
        w = (w * mask.float())
        w = torch.nn.functional.dropout(w, p=self.dropout_probability)
        z = torch.matmul(w, v)
        z = F.normalize(z, p=2, dim=3)
        z = torch.cat([x1, z], dim=1)
        out = self.out_conv(z, x2, dropout_p=self.dropout_probability)
        return out



dropout_p = 1

func = Model(dropout_p).to('cuda')

x1 = 1
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'size'

jit:
'int' object has no attribute 'size'

from user code:
   File "<string>", line 65, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.head_num = 16
        self.size_per_head = 64
        self.qkv_weights = torch.nn.Linear(48, ((3 * self.head_num) * self.size_per_head))
        self.out_weights = torch.nn.Linear((self.head_num * self.size_per_head), 1600)

    def forward(self, l):
        sz = l.size()
        qkvw = self.qkv_weights(l)
        qkv = qkvw.view(sz[0], sz[1], 3, self.head_num, self.size_per_head)
        q = qkv[:, :, 0]
        k = qkv[:, :, 1]
        v = qkv[:, :, 2]
        d = q.size((- 1))
        attn_mask = (torch.triu(torch.full((d, d), 1000000000.0, device=x.device, dtype=x.dtype)) * torch.triu(torch.full((d, d), 0, device=x.device, dtype=x.dtype), 1))
        attn_mask = attn_mask.unsqueeze(0).expand(sz[0], 1, d, d)
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        return ((attn_weight @ v).view(sz) @ self.out_weights(q))



func = Model().to('cuda')



x1 = torch.randn(1, 128, 48)


test_inputs = [x1]

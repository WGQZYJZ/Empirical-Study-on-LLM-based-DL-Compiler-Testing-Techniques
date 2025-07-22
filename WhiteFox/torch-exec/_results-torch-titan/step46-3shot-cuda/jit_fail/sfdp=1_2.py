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



class T5Attention(nn.Module):

    def __init__(self, q, k, v, mask, dropout_p=0.2):
        super().__init__()
        self.scale_factor = math.sqrt(q.size((- 1)))
        self.dropout = nn.Dropout(dropout_p)
        q = q.float()
        k = k.float()
        self.q = self.dropout(q)
        self.k = self.dropout(k)
        self.scale_factor = self.dropout(torch.tensor([self.scale_factor]))
        self.v = self.dropout(v)
        self.mask = mask

    def forward(self, x):
        qk = torch.matmul(x, self.k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        masked_softmax_qk = softmax_qk.masked_fill(self.mask, float('-inf'))
        output = torch.matmul(masked_softmax_qk, self.v)
        return output




q = torch.randn(2, 3, 512, 1, dtype=torch.float)


k = torch.randn(2, 3, 1, 512, dtype=torch.float)


v = torch.randn(2, 3, 512, 512, dtype=torch.float)


mask = torch.randint(0, 2, (2, 1, 1, 512))

func = T5Attention(q, k, v, mask).to('cuda')




q = torch.randn(2, 3, 512, 1, dtype=torch.float)




k = torch.randn(2, 3, 1, 512, dtype=torch.float)




v = torch.randn(2, 3, 512, 512, dtype=torch.float)



mask = torch.randint(0, 2, (2, 1, 1, 512))


test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''
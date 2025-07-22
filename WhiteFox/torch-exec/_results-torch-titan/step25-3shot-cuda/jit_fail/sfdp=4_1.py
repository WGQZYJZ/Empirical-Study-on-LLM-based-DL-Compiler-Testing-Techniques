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

    def __init__(self, nhead, nhid, dropout):
        super().__init__()
        self.nhead = nhead
        self.nhid = nhid
        self.dropout = dropout
        self.h = torch.nn.ModuleList([torch.nn.Linear(nhid, nhid) for _ in range(nhead)])
        self.attn_dropout = torch.nn.Dropout(dropout)
        self.o = torch.nn.Linear(nhid, nhid)

    def forward(self, x1, x2, x3):
        bs = x1.size(0)
        x4 = torch.empty(bs, self.nhead, self.nhid, device=x1.device)
        for i in range(self.nhead):
            head = self.h[i](x2).view(bs, (- 1), (self.nhid // self.nhead))
            q = (head @ head.transpose((- 2), (- 1)))
            k = (head @ head.transpose((- 2), (- 1)))
            v = (head @ head.transpose((- 2), (- 1)))
            w = (((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1)))) + x3)
            a = torch.softmax(w, dim=(- 1))
            x4[:, i, :] = (a @ head)
        x = x4.transpose(1, 2).contiguous().view(bs, (- 1))
        x = self.o(x)
        return x




nhead = 2


nhid = 128


dropout = 0.2

func = Model(nhead, nhid, dropout).to('cuda')



x1 = torch.randn(5, 24, 128)



x2 = torch.randn(5, 24, 128)


x2 = torch.randn(5, 24, 128)


x2 = torch.randn(5, 24, 128)


nhead = 2


nhead = 2



attn_mask = torch.randint(0, 1, (5, (nhead * (1 + x2.size(1))), (nhead * (1 + x2.size(1)))))


test_inputs = [x1, x2, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (48) must match the size of tensor b (50) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(5, 48, 48)), FakeTensor(..., device='cuda:0', size=(5, 50, 50), dtype=torch.int64)), **{}):
Attempting to broadcast a dimension of length 50 at -1! Mismatching argument at index 1 had torch.Size([5, 50, 50]); but expected shape should be broadcastable to [5, 48, 48]

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
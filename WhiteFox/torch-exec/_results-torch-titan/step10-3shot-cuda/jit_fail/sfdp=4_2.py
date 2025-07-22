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

    def forward(self, query, key, value, attn_mask):
        dim = query.size((- 1))
        scores = (query.matmul(key.transpose((- 2), (- 1))) / math.sqrt(dim))
        scores += attn_mask
        p_attn = F.softmax(scores, dim=(- 1))
        return p_attn.matmul(value)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.embedding = torch.nn.Embedding(1026, 768)
        self.lin1 = torch.nn.Linear(768, 16)
        self.lin2 = torch.nn.Linear(16, 16)
        self.lin3 = torch.nn.Linear(16, 2)
        self.attn = Attention()

    def forward(self, x1, x2, x3, x4):
        input_embeds = self.embedding(x1)
        attn_mask = F.dropout(make_pad_mask(x2), p=0.1, training=self.training)
        l1 = self.lin1(input_embeds)
        l2 = F.glu(l1, dim=(- 1))
        l3 = self.lin2(l2)
        l4 = F.glu(l3, dim=(- 1))
        l5 = self.lin3(l4)
        l7 = self.attn(l5, l5, l5, attn_mask)
        return torch.stack([l7, l5], dim=2)



func = Model().to('cuda')




x1 = torch.randint(1026, (3, 128), dtype=torch.long)



x2 = torch.zeros((128, 128))




x3 = torch.zeros(1026, 768, dtype=torch.float)



x4 = torch.ones((768, 768))


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
name 'make_pad_mask' is not defined

jit:
name 'make_pad_mask' is not defined

from user code:
   File "<string>", line 42, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
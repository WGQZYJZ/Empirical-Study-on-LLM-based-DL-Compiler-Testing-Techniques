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
        self.linear1 = nn.Linear(in_features, out_features)
        self.linear2 = nn.Linear(in_features, out_features)

    def forward(self, q, k, v1, mask):
        q = self.linear1(q)
        q = self.linear2(q)
        k = self.linear1(k)
        k = self.linear2(k)
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v1)
        return output




func = Model().to('cuda')



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))

q = 1
k = 1
v1 = 1

test_inputs = [mask, q, k, v1]

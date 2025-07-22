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
        self.dropout_p = 0.5

    def forward(self, input, w):
        k = torch.einsum('ijk,lkj->ijl', input, w)
        k = k / (self.dropout_p + inp[0].sum(dim=-1, keepdim=True))
        v = torch.einsum('ijk,lkj->ijl', input, w)
        q = torch.einsum('ijk,ijl->ijl', input, w)
        q = q / (self.dropout_p + inp[1].sum(dim=-1, keepdim=True))
        mask = q.new(q.shape[0], q.shape[1], q.shape[1]).fill_(float('-inf')).triu(diagonal=1)
        mask = mask.cuda()
        return torch.softmax(q + mask, dim=-1).matmul(v)


func = Model().to('cpu')


q = torch.rand(3, 50, 10)

k = torch.rand(3, 7, 10)

v = torch.rand(3, 7, 10)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''
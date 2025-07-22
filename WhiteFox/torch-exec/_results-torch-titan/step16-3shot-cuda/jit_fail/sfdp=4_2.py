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
        self.query = torch.nn.Linear(4, 4)
        self.key = torch.nn.Linear(4, 4)
        self.value = torch.nn.Linear(4, 4)

    def forward(self, query, key, value):
        qk = ((self.query(query) @ self.key(key).transpose((- 2), (- 1))) / math.sqrt(self.query.weight.shape[(- 1)]))
        qk = (qk + attention_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ self.value(value))
        return output



func = Model().to('cuda')



query = torch.randn(3, 5, 4)



key = torch.randn(3, 1, 4)



value = torch.randn(3, 1, 4)




attention_mask = torch.zeros(3, 5, 1, dtype=torch.long)


test_inputs = [query, key, value, attention_mask]

# JIT_FAIL
'''
direct:
forward() takes 4 positional arguments but 5 were given

jit:
forward() takes 4 positional arguments but 5 were given
'''
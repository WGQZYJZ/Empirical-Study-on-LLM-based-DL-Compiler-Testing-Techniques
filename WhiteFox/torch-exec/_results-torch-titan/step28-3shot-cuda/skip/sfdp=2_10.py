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
        self.query_key = Linear(1024, 1024)
        self.softmax_dropout_value = Linear(1024, 1024)

    def forward(self, x1, x2):
        k = self.query_key(x1)
        v = self.softmax_dropout_value(x2)
        d = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_d = (1.0 / math.sqrt(d.size()[(- 1)]))
        d = torch.div(d, inv_d)
        s = d.softmax(dim=(- 1))
        dropout_s = torch.nn.functional.dropout(s, p=0.3)
        o = dropout_s.matmul(v)
        return o



func = Model().to('cuda')



x1 = torch.randn(1, 1024)



x2 = torch.randn(1, 1024)


test_inputs = [x1, x2]

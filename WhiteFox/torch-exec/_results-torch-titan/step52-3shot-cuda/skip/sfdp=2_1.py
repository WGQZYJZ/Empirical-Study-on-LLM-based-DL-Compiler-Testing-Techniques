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
        self.matmul = torch.nn.MatMul(None, True)

    def forward(self, q1, k1, v1, inver_scale_factor, dropout_scale_factor):
        v1 = self.matmul(q1, k1.transpose((- 2), (- 1)))
        v2 = v1.div(inver_scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = F.dropout(v3, dropout_p, False)
        dropout_qk = self.matmul(v4, v1)
        output = self.matmul(dropout_qk, v1)
        return output



func = Model().to('cuda')



q1 = torch.randn(1, 1, 8)



k1 = torch.randn(1, 8, 8)

v1 = 1
inver_scale_factor = 1
dropout_scale_factor = 1

test_inputs = [q1, k1, v1, inver_scale_factor, dropout_scale_factor]

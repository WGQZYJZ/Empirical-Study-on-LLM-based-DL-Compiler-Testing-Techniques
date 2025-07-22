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
        scale_factor = (1.0 / math.sqrt(512))
        self.q = torch.nn.Linear(512, 384)
        self.k = torch.nn.Linear(512, 384)
        self.value = torch.nn.Linear(512, 384)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.scale_factor = scale_factor

    def forward(self, q, k, v):
        q_temp = F.normalize(self.q(q), dim=(- 1), p=2).div(self.scale_factor)
        k_temp = F.normalize(self.k(k), dim=(- 1), p=2).div(self.scale_factor)
        v_temp = F.normalize(self.value(v), dim=(- 1), p=2).div(self.scale_factor)
        qk = torch.matmul(qk, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')

q = 1
k = 1
v = 1

test_inputs = [q, k, v]

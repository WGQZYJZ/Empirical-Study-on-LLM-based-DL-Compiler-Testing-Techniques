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
        self.dropout = torch.nn.Dropout(p)

    def forward(self, q, k, v, scale):
        scaled_qk = (torch.matmul(q, k.transpose((- 2), (- 1))) / scale)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output




func = Model().to('cuda')

q = 1
k = 1
v = 1
scale = 1

test_inputs = [q, k, v, scale]

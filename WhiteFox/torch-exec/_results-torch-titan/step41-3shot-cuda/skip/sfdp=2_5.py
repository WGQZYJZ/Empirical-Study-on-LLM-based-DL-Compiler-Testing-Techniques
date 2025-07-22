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
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 8, 17, 13)



k = torch.randn(1, 11, 21, 7)



v = torch.randn(1, 11, 21, 7)


test_inputs = [q, k, v]

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
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, q, k, v, inv_scale_factor):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 2, 512)



k = torch.randn(1, 4, 512)



v = torch.randn(1, 4, 512)



inv_scale_factor = torch.randn(1, 1)


test_inputs = [q, k, v, inv_scale_factor]

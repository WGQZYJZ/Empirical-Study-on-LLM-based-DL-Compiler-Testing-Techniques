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

    def __init__(self, input_length=3, input_width=72, num_units=12, dropout=0.2, scale_factor=None):
        super(Model, self).__init__()
        self.dropout = torch.nn.Dropout(p=dropout)
        if (scale_factor is not None):
            self.scale_factor = scale_factor
        else:
            self.scale_factor = maxsize

    def forward(self, x1, x2):
        qk = x1.bmm(x2.transpose(1, 2))
        if (self.scale_factor != maxsize):
            qk = (qk * self.scale_factor)
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.bmm(x2)
        return output



func = Model().to('cuda')

x1 = 1
x2 = 1

test_inputs = [x1, x2]

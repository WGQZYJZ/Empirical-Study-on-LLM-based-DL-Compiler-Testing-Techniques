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
        self.query = Param(torch.randn(4096, 512))
        self.key = Param(torch.randn(4096, 512))
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)
        self.value = Param(torch.randn(512, 4096))

    def forward(self, in1, in2):
        qk = torch.matmul(in1, in2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        output = self.dropout(softmax_qk).matmul(self.value)
        return output



func = Model().to('cuda')



x1 = torch.randn(2048, 512)



x2 = torch.randn(2048, 512)


test_inputs = [x1, x2]

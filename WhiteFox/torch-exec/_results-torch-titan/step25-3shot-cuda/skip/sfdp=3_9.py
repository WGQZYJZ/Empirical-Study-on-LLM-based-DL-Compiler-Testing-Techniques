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

    def __init__(self, config):
        super().__init__()
        d_model = config.d_model
        nhead = config.nhead
        self.scale_factor = (1 / (d_model ** 0.5))
        self.dropout_p = 0.1

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = F.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(x2)
        return output




config = Config()

func = Model(config).to('cuda')



x1 = torch.randn(2052, 12, 128)



x2 = torch.randn(2052, 12, 128)


test_inputs = [x1, x2]

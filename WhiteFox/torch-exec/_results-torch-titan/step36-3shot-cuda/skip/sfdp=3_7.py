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
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = (v1 * scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = self.dropout(v3)
        v5 = torch.matmul(v4, x2)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 7, 10)



x2 = torch.randn(1, 16, 7)


test_inputs = [x1, x2]

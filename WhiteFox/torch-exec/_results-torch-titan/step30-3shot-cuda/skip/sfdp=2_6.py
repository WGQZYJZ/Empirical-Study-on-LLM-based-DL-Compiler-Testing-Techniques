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
        self.query = torch.nn.Linear(128, 100)
        self.key = torch.nn.Linear(128, 100)
        self.value = torch.nn.Linear(128, 100)
        self.dropout = torch.nn.Dropout(drop_p=0.2)
        self.scale_factor = torch.sqrt(torch.tensor(100))

    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
        v3 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v4 = (v3 / self.scale_factor)
        v5 = v4.softmax(dim=(- 1))
        v6 = self.dropout(v5)
        v7 = torch.matmul(v6, self.value(x2))
        return v7



func = Model().to('cuda')



x1 = torch.rand(64, 128)



x2 = torch.rand(64, 128)


test_inputs = [x1, x2]

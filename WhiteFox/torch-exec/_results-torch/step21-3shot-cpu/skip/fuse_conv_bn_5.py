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
        self.convs = torch.nn.ModuleList([torch.nn.Conv2d(8, out_c, 3, padding=1), torch.nn.Conv2d(out_c, out_c, 3, padding=1), torch.nn.Conv2d(out_c, out_c, (1, 7), padding=(0, 3)), torch.nn.Conv2d(out_c, out_c, (7, 1), padding=(3, 0)), torch.nn.Conv2d(out_c, out_c, (3, 3), padding=1), torch.nn.Conv2d(out_c, out_c, (3, 3), dilation=2, padding=2)])
        self.bns = torch.nn.ModuleList([torch.nn.BatchNorm2d(out_c), torch.nn.BatchNorm2d(out_c), torch.nn.BatchNorm2d(out_c), torch.nn.BatchNorm2d(out_c), torch.nn.BatchNorm2d(out_c), torch.nn.BatchNorm2d(out_c)])

    def forward(self, v):
        for i in range(len(self.convs)):
            v = self.convs[i](v)
            v = self.bns[i](v)
            v = F.relu(v)
        return v



func = Model().to('cpu')


v = torch.randn(4, 8, 5, 5)

test_inputs = [v]

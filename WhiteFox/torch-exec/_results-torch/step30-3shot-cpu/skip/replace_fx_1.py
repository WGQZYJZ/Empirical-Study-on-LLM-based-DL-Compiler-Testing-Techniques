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
        self.layer = torch.nn.modules.resnet.Bottleneck(16, 64, 2)

    def forward(self, x1):
        v = torch.nn.functional.dropout(x1, p=0, training=False)
        x = self.layer(v)
        y = torch.matmul(x, x)
        return y



func = Model().to('cpu')


x1 = torch.randn(1, 16, 4, 4)

test_inputs = [x1]

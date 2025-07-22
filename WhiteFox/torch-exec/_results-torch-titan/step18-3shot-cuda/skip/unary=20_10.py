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
        super().__init_subclass__()
        self.conv_t = torch.nn.ConvTranspose2d(1, 1, kernel_size=(5, 5), stride=(1, 1), bias=True, padding=(2, 2))

    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 1, 301, 604)


test_inputs = [x1]

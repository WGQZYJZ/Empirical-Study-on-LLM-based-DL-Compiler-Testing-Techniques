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
        self.conv_t1 = torch.nn.ConvTranspose2d((17, 20), 13, (1, 6), stride=(1, 2), bias=True)
        self.conv_t2 = torch.nn.ConvTranspose2d(17, 9, (1, 7), stride=(1, 1), bias=False)
        self.conv_t3 = torch.nn.ConvTranspose2d((41, 60), 11, (5, 7), stride=(3, 4), bias=False, output_padding=(10, 9))

    def forward(self, x1):
        x = torch.sigmoid(self.conv_t1(x1))
        x = torch.sigmoid(self.conv_t2(x))
        x = torch.sigmoid(self.conv_t3(x))
        return x




func = Model().to('cuda')



x1 = torch.randn(2, 17, 51, 53)


test_inputs = [x1]

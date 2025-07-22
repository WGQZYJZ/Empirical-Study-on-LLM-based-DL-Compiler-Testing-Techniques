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
        t1 = torch.nn.Conv2d(1, 20, kernel_size=(1,), stride=(1,))
        t2 = torch.nn.ReLU()
        self.t3 = torch.nn.Conv2d(20, 20, kernel_size=(3,), stride=(1,))
        t4 = torch.nn.ReLU()
        self.t5 = torch.nn.ConvTranspose2d(20, 1, kernel_size=(3,), stride=(1,), padding=(0,), out_padding=(0,))
        self.t6 = torch.nn.ReLU()
        self.t7 = torch.nn.Conv2d(1, 1, kernel_size=((1 + 1),), stride=(1,))

    def forward(self, x1):
        v1 = self.t3(x1)
        v2 = self.t6(v1)
        v3 = self.t7(v2)
        v4 = torch.add(v3, v1)
        v5 = torch.add(v4, v2)
        v6 = torch.add(v5, x1)
        v7 = torch.add(x1, v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 1, 512, 512)


test_inputs = [x1]

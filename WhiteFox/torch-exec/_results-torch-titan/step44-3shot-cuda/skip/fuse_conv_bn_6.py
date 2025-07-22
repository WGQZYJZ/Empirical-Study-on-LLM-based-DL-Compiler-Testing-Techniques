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
        self.layer1 = torch.nn.TransformerEncoder()
        self.layer2 = torch.nn.TransformerEncoderLayer(20, 5)

    def forward(self, x0):
        x = self.layer1(x0)
        y = self.layer2(x)
        return y




func = Model().to('cuda')



x0 = torch.randn(4, 6, 20)



x1 = torch.randn(7, 6, 20)


test_inputs = [x0, x1]

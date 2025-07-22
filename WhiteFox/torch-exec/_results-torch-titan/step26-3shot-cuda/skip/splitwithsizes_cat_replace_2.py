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



class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.model_0 = MMDNNModel('mnist_lenet.pb')
        self.model_1 = MMDNNModel('mnist_lenet.pb')
        self.model_2 = MMDNNModel('mnist_lenet.pb')

    def forward(self, v1):
        split_tensors = torch.split(v1, [1], dim=1)
        concatenated_tensor = split_tensors[0]
        return (concatenated_tensor, torch.split(v1, [1], dim=1))




func = Model().to('cuda')



x = torch.randn(2, 1, 224, 224)


test_inputs = [x]

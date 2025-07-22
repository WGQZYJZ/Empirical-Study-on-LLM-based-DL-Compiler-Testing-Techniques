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
        self.linear1 = torch.nn.Linear(512, 512)
        self.linear2 = torch.nn.Linear(512, 256)
        self.linear3 = torch.nn.Linear(128, 128)
        self.linear4 = torch.nn.Linear(64, 64)
        self.query = torch.nn.Linear(512, 256)
        self.key = torch.nn.Linear(512, 256)
        self.value = torch.nn.Linear(512, 256)
        self.dropout = torch.nn.Dropout(0.2)

    def forward(self, input_tensor1):
        linear_tensor1 = torch.relu(self.linear1(input_tensor1))
        linear_tensor2 = torch.relu(self.linear2(linear_tensor1))
        query = self.query(linear_tensor2)
        key = self.key(linear_tensor2)
        value = self.value(linear_tensor2)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = torch.sqrt(torch.FloatTensor([list(query.size())[(- 1)]]))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        linear3_tensor2 = torch.relu(self.linear3(linear_tensor2))
        linear4_tensor2 = torch.relu(self.linear4(linear3_tensor2))
        return (output, linear4_tensor2)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 64)
        self.linear2 = torch.nn.Linear(64, 16)
        self.linear3 = torch.nn.Linear(64, 16)
        self.linear4 = torch.nn.Linear(32, 32)
        self.conv1 = torch.nn.ConvTranspose2d(32, 32, 8, stride=4, output_padding=1)
        self.conv2 = torch.nn.ConvTranspose2d(16, 12, 3, stride=2)
        self.conv3 = torch.nn.ConvTranspose2d(12, 3, 3, stride=2)
        self.bn1 = torch.nn.BatchNorm2d(32, momentum=0.1)
        self.bn2 = torch.nn.BatchNorm2d(16, momentum=0.1)
        self.bn3 = torch.nn.BatchNorm2d(16)

    def forward(self, input1, input2):
        conv1_tensor1 = torch.tanh(self.conv1(input1))
        bn1_tensor1 = self.bn1(conv1_tensor1)
        conv2_tensor1 = torch.relu(self.conv2(bn1_tensor1))
        bn2_tensor1 = self.bn2(conv2_tensor1)
        conv3_tensor1 = self.conv3(torch.relu(bn2_tensor1))
        bn3_tensor1 = self.bn3(conv3_tensor1)
        flatten_tensor1 = conv3_tensor1.flatten(1, 3)
        linear1_tensor1 = torch.leaky_relu(self.linear1(flatten_tensor1))
        drop1_tensor1 = torch.nn.functional.dropout(linear1_tensor1)
        linear2_tensor1 = torch.nn.functional.leaky_relu(self.linear2(linear1_tensor1))
        linear3_tensor1 = torch.nn.functional.leaky_relu(self.linear3(linear2_tensor1))
        linear4_tensor1 = torch.nn.functional.relu(self.linear4(linear3_tensor1))
        concat_tensor1 = torch.cat((flatten_tensor1, linear4_tensor1), dim=1)
        x = torch.flatten(self.bn3(self.conv2(linear2_tensor1)), 1)
        x = x.unsqueeze(2).unsqueeze(3)
        linear_tensor1 = (input2 * x)
        linear5_tensor = torch.flatten(self.linear5(linear_tensor1), 1)
        drop2_tensor1 = torch.nn.functional.dropout(linear5_tensor)
        linear6_tensor = torch.flatten(self.linear6(drop2_tensor1), 1)
        concat2_tensor1 = torch.cat((drop2_tensor1, drop2_tensor1, linear6_tensor), dim=1)
        return concat2_tensor1



func = Model().to('cuda')



input_tensor = torch.randn(1, 512)



input1 = torch.randn(256, 32, 4, 4)



input2 = torch.randn(256, 3, 64, 64)


test_inputs = [input_tensor, input1, input2]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''
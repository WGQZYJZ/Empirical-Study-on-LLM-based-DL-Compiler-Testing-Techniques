'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad3d\ntorch.nn.ReplicationPad3d(padding)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch
input_data = Variable(torch.Tensor(1, 1, 4, 4, 4).random_(0, 255))
torch.nn.ReplicationPad3d(padding=2)
print('input_data: ', input_data)
print('input_data.shape: ', input_data.shape)
pad3d = torch.nn.ReplicationPad3d(padding=2)
out = pad3d(input_data)
print('out: ', out)
print('out.shape: ', out.shape)
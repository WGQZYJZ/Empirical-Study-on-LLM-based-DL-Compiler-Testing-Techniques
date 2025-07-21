'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.nn.parameter import Parameter
import numpy as np
input_data = Variable(torch.randn(1, 1, 4, 4))
padding = (1, 1, 1, 1)
replication_pad = nn.ReplicationPad2d(padding)
output_data = replication_pad(input_data)
print('input_data:', input_data)
print('output_data:', output_data)
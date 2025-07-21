'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout3d\ntorch.nn.Dropout3d(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.randn(1, 1, 2, 2, 2))
dropout3d = torch.nn.Dropout3d(p=0.5, inplace=False)
output = dropout3d(input_data)
print(output)
print(output.size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
input_data = Variable(torch.randn(5, 3))
print(input_data)
dropout = nn.Dropout(p=0.5)
print(dropout(input_data))
dropout = nn.Dropout(p=0.5, inplace=True)
print(dropout(input_data))
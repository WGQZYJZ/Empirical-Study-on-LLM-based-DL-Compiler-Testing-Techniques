'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.alpha_dropout\ntorch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch
input_data = Variable(torch.randn(1, 1, 4, 4))
output_data = F.alpha_dropout(input_data, p=0.5, training=False, inplace=False)
print(input_data)
print(output_data)
print(torch.sum(input_data))
print(torch.sum(output_data))
print(input_data.size())
print(output_data.size())
print(torch.sum((input_data == output_data)))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=False, inplace=False)\n'
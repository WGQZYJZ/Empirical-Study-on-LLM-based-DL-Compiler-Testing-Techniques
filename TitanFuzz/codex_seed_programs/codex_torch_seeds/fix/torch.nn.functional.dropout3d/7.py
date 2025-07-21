'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout3d\ntorch.nn.functional.dropout3d(input, p=0.5, training=True, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
input = Variable(torch.randn(1, 2, 3, 3, 3))
print('Input: ', input)
output = F.dropout3d(input, p=0.5, training=True)
print('Output: ', output)
output = F.dropout3d(input, p=0.5, training=False)
print('Output: ', output)
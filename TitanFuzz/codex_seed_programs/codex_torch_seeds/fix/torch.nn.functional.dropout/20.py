'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
from torch.autograd import Variable
x = Variable(torch.randn(5, 5))
print(x)
output = F.dropout(x, training=True)
print(output)
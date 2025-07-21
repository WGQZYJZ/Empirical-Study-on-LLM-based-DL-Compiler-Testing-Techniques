'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout2d\ntorch.nn.functional.dropout2d(input, p=0.5, training=True, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 3, 3))
print(x)
dropout2d = torch.nn.functional.dropout2d(x, p=0.5, training=True, inplace=False)
print(dropout2d)
dropout2d = torch.nn.functional.dropout2d(x, p=0.5, training=False, inplace=False)
print(dropout2d)
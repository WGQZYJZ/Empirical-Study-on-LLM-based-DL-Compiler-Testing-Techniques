'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.alpha_dropout\ntorch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
x = Variable(torch.randn(5, 5))
print(F.alpha_dropout(x, training=True))
print(F.alpha_dropout(x, training=False))
print(F.alpha_dropout(x, p=0.5, training=True))
print(F.alpha_dropout(x, p=0.5, training=False))
print(F.alpha_dropout(x, p=0.5, inplace=True))
print(F.dropout(x, p=0.5, training=True))
print(F.dropout(x, p=0.5, training=False))
print(F.dropout(x, p=0.5, inplace=True))
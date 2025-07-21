'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.ones(2, 2))
y = torch.nn.functional.dropout(x, p=0.5, training=True, inplace=False)
print(y)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiMarginLoss\ntorch.nn.MultiMarginLoss(p=1, margin=1.0, weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch
import torch.nn as nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.LongTensor(3).random_(5))
loss = nn.MultiMarginLoss()
output = loss(input, target)
output.backward()
print(output)
print(input.grad)
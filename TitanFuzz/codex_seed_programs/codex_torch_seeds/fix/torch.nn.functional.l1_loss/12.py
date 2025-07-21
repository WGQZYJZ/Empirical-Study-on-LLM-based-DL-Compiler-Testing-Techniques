"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.l1_loss\ntorch.nn.functional.l1_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.randn(3, 5))
loss = torch.nn.functional.l1_loss(input, target)
print(loss)
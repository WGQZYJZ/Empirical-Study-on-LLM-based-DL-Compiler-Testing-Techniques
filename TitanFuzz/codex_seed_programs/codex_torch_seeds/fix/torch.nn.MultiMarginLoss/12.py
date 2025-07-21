"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiMarginLoss\ntorch.nn.MultiMarginLoss(p=1, margin=1.0, weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 3))
y = Variable(torch.LongTensor(5).random_(3))
loss = torch.nn.MultiMarginLoss()
output = loss(x, y)
print(output)
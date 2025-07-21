"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(3, 5), requires_grad=True)
y = Variable(torch.LongTensor(3).random_(5))
loss = torch.nn.functional.cross_entropy(x, y)
print(loss)
loss = torch.nn.functional.cross_entropy(x, y, size_average=False)
print(loss)
loss = torch.nn.functional.cross_entropy(x, y, reduce=False)
print(loss)
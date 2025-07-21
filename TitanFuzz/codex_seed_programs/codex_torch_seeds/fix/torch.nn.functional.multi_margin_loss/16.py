"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.multi_margin_loss\ntorch.nn.functional.multi_margin_loss(input, target, p=1, margin=1.0, weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.LongTensor(3).random_(5))
print('Input data: ', input)
print('Target data: ', target)
loss = torch.nn.functional.multi_margin_loss(input, target)
print('Loss: ', loss)
loss.backward()
print('Loss backward: ', input.grad)
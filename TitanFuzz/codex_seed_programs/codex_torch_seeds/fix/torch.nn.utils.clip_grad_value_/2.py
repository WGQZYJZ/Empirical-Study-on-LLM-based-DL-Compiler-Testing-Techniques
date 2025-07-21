'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
from torch.autograd import Variable
from torch.nn.utils import clip_grad_value_
x = Variable(torch.randn(4, 4))
w = Variable(torch.randn(4, 4), requires_grad=True)
y = torch.sum((x * w))
y.backward()
print(w.grad)
clip_grad_value_(w, 0.5)
print(w.grad)
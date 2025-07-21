'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0, error_if_nonfinite=False)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1), requires_grad=True)
y = Variable(torch.randn(1, 1), requires_grad=True)
z = Variable(torch.randn(1, 1), requires_grad=True)
a = (x + y)
b = (a + z)
b.backward()
print(x.grad, y.grad, z.grad)
torch.nn.utils.clip_grad_norm_(x, max_norm=1)
torch.nn.utils.clip_grad_norm_(y, max_norm=1)
torch.nn.utils.clip_grad_norm_(z, max_norm=1)
print(x.grad, y.grad, z.grad)
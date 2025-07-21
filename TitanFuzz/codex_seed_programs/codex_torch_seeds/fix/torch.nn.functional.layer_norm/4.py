'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import layer_norm
x = Variable(torch.randn(10, 5))
weight = Variable(torch.randn(5), requires_grad=True)
bias = Variable(torch.randn(5), requires_grad=True)
y = layer_norm(x, [5], weight, bias)
print(y)
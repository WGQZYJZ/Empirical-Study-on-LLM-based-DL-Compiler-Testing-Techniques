'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch
x = torch.rand(1, 1, 3, 3)
y = torch.rand(1, 1, 3, 3)
x = torch.jit.annotate(torch.Tensor, x)
y = torch.jit.annotate(torch.Tensor, y)
print(x)
print(y)
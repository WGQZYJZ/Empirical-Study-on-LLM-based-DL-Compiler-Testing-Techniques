'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
x = Variable(torch.randn(1, 1, 3, 3))
print(x)
y = F.upsample_bilinear(x, scale_factor=2)
print(y)
y = F.upsample_bilinear(x, size=4)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 3, 10, 10, 10))
y = torch.nn.AdaptiveAvgPool3d(output_size=1)(x)
print(x.shape)
print(y.shape)
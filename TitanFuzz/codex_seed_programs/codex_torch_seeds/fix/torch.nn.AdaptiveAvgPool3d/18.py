'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.autograd import Variable
import torch
x = torch.randn(1, 3, 5, 5, 5)
y = torch.randn(1, 3, 5, 5, 5)
z = torch.nn.AdaptiveAvgPool3d(output_size=2)
print(z(x))
print(z(y))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.autograd import Variable
import torch
input = torch.randn(1, 1, 4, 4, 4)
output = torch.nn.AdaptiveAvgPool3d(output_size=1)(input)
print(output)
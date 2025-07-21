'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 4, 4, 4))
avg_pool3d = torch.nn.AdaptiveAvgPool3d(output_size=(1, 1, 1))
output = avg_pool3d(input)
print(output.data)
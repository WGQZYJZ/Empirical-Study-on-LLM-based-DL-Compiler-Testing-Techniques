'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4, 4))
avg_pool = torch.nn.AdaptiveAvgPool3d(output_size=(2, 2, 2))
avg_pool(input)
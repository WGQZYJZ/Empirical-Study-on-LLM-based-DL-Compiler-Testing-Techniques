'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(1, 3, 5, 5, 5))
max_pool_3d = torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3))
output = max_pool_3d(input)
print(output)
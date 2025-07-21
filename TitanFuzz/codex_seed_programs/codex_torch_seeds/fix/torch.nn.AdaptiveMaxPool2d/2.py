'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
print(input)
output = torch.nn.AdaptiveMaxPool2d(2)(input)
print(output)
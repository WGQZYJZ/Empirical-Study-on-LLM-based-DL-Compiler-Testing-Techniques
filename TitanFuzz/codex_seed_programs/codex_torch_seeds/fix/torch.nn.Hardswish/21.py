'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
input = torch.randn(3, 3)
output = torch.nn.Hardswish()(input)
print(output)
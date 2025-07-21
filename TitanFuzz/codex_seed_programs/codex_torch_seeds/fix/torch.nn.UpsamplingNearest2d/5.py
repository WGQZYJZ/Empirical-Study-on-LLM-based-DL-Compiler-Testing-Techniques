'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
input_data = Variable(torch.Tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]]))
upsampling_nearest2d = nn.UpsamplingNearest2d(size=(5, 5))
output = upsampling_nearest2d(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
x = Variable(torch.Tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]))
upsample = nn.UpsamplingNearest2d(scale_factor=2)
output = upsample(x)
print(output)
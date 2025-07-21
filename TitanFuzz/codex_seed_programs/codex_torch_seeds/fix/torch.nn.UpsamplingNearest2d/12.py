'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
x = torch.tensor([[[1, 2], [3, 4]]], dtype=torch.float32)
upsampling = nn.UpsamplingNearest2d(scale_factor=2)
y = upsampling(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
x = torch.tensor([[[1, 2], [3, 4]]], dtype=torch.float32)
upsampling = nn.UpsamplingBilinear2d
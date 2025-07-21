"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 1, 2, 2)
upsample_layer = nn.Upsample(size=(4, 4), mode='bilinear')
output = upsample_layer(input)
print(input)
print(output)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 1, 2, 2)
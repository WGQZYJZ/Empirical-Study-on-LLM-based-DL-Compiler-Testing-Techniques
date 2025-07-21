'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
input = torch.randn(20, 5, 3, 3)
m = nn.BatchNorm2d(5)
output = m(input)
print(output.size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
input
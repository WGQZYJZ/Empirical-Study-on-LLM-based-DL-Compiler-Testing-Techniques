"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(1, 3, 224, 224)
weight = torch.empty(3, 3)
nn.init.kaiming_normal_(weight, mode='fan_in', nonlinearity='relu')
print(weight)
weight = torch.empty(3, 3)
nn.init.kaiming_uniform_(weight, mode='fan_in', nonlinearity='relu')
print(weight)
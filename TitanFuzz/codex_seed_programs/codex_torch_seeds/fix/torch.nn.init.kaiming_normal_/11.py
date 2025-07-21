"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import torch.nn as nn
import numpy as np
input_tensor = torch.randn(3, 5)
torch.nn.init.kaiming_normal_(input_tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')
print(input_tensor)
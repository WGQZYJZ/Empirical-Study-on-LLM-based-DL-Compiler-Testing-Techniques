'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
from torch import nn
import torch
from torch import nn
input_tensor = torch.randn(2, 3)
print(input_tensor)
torch.nn.init.constant_(input_tensor, 0.5)
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.eye_\ntorch.nn.init.eye_(tensor)\n'
import torch
from torch import nn
import torch
from torch import nn
input_tensor = torch.randn(2, 3)
print(input_tensor)
torch.nn.init.eye_(input_tensor)
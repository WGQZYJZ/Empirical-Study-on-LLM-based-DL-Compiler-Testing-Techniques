'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix_\ntorch.Tensor.fix_(_input_tensor)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
import numpy as np
input_tensor = torch.randn(1, 1, 28, 28)
torch.Tensor.fix_(input_tensor)
print('input_tensor:', input_tensor)
print('input_tensor.type:', input_tensor.type())
print('input_tensor.dtype:', input_tensor.dtype)
print('input_tensor.device:', input_tensor.device)
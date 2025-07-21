'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_inference_mode_enabled\ntorch.is_inference_mode_enabled()\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
data = Variable(torch.randn(1, 1, 1, 1))
torch.is_inference_mode_enabled()
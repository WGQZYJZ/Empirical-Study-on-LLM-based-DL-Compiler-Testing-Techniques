"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.spectral_norm\ntorch.nn.utils.spectral_norm(module, name='weight', n_power_iterations=1, eps=1e-12, dim=None)\n"
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(1, 3, 224, 224))
from torch.nn.utils import spectral_norm
module = spectral_norm(torch.nn.Conv2d(3, 64, 3, 1, 1))
module(input_data)
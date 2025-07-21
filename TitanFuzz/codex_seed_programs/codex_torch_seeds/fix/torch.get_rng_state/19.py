'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
import numpy as np
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
y = torch.Tensor([[1, 2, 3], [4, 5, 6]])
torch.get_rng_state()
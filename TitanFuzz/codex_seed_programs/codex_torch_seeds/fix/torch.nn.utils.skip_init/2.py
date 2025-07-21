'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.skip_init\ntorch.nn.utils.skip_init(module_cls, *args, **kwargs)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
torch.nn.utils.skip_init(nn.Linear, *(2, 3), **{'bias': False})
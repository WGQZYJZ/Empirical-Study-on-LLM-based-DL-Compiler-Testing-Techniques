'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import sampler
import torchvision.datasets as dset
import torchvision.transforms as T
import numpy as np
import timeit
input_data = torch.randn(5, 3)
input_data_type = torch.jit.annotate(torch.Tensor, input_data)
print(input_data_type)
print(input_data)
print(type(input_data))
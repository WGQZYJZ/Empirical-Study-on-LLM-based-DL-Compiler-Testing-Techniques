'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ConcatDataset\ntorch.utils.data.ConcatDataset(datasets)\n'
import torch
import torch.utils.data as data
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.utils.data as data
import torchvision.datasets as dsets
import torchvision.transforms as transforms
input_data = torch.randn(2, 3, 5)
print(input_data)
dataset = data.ConcatDataset([input_data, input_data])
print(dataset)
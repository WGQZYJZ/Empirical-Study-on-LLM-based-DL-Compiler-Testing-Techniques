'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.are_deterministic_algorithms_enabled\ntorch.are_deterministic_algorithms_enabled()\n'
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision import transforms
import numpy as np
batch_size = 256
train_dataset = MNIST(root='../../data', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = MNIST(root='../../data', train=False, transform=transforms.ToTensor(), download=True)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
torch.are_deterministic_algorithms_enabled()
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch.autograd import Variable
torch.set_num_interop_threads(4)
batch_size = 64
learning_rate = 0.01
num_epochs = 20
train_dataset = datasets.MNIST(root='../../data/', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST(root='../../data/', train=False, transform=transforms.ToTensor())
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
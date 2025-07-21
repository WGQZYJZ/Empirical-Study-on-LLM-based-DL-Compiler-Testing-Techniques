import torch
from torch import nn
from torch.autograd import Variable
train_dataset = torchvision.datasets.MNIST(root='/tmp/', train=True, transform=torchvision.transforms.ToTensor(), download=True)
test_dataset = torchvision.datasets.MNIST(root='/tmp/', train=False, transform=torchvision.transforms.ToTensor(), download=True)
train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset, num_replicas=2, rank=0)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.distributed.DistributedSampler\ntorch.utils.data.distributed.DistributedSampler(dataset, num_replicas=None, rank=None, shuffle=True, seed=0, drop_last=False)\n'
import torch
import torch.distributed as dist
import torch.utils.data
import torch.utils.data.distributed
import torchvision
import torch
import torch.distributed as dist
import torch.utils.data
import torch.utils.data.distributed
import torchvision
train_dataset = torchvision.datasets.MNIST(root='/tmp/', train=True, transform=torchvision.transforms.ToTensor(), download=True)
test_dataset = torchvision.datasets.MNIST(root='/tmp/', train=False, transform=torchvision.transforms.ToTensor(), download=True)
train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset, num_replicas=2, rank=0)
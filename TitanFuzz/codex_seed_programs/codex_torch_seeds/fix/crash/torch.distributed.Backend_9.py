'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.Backend\ntorch.distributed.Backend(name)\n'
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.backends.cudnn as cudnn
import torchvision
import torchvision.transforms as transforms
import os
import argparse
from torch.multiprocessing import Process
from torch.autograd import Variable
parser = argparse.ArgumentParser(description='PyTorch CIFAR10 Training')
parser.add_argument('--lr', default=0.1, type=float, help='learning rate')
parser.add_argument('--resume', '-r', action='store_true', help='resume from checkpoint')
args = parser.parse_args()
use_cuda = torch.cuda.is_available()
best_acc = 0
start_epoch = 0
print('==> Preparing data..')
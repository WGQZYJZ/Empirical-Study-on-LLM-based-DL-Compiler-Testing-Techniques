'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.reduce_scatter_multigpu\ntorch.distributed.reduce_scatter_multigpu(output_tensor_list, input_tensor_lists, group=None, async_op=False)\n'
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
parser = argparse.ArgumentParser(description='PyTorch CIFAR10 Training')
parser.add_argument('--lr', default=0.1, type=float, help='learning rate')
parser.add_argument('--resume', '-r', action='store_true', help='resume from checkpoint')
args = parser.parse_args()
device = ('cuda' if torch.cuda.is_available() else 'cpu')
best_acc = 0
start_epoch = 0
print('==> Preparing data..')
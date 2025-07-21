'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SyncBatchNorm\ntorch.nn.SyncBatchNorm(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, process_group=None, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.backends.cudnn as cudnn
from torch.nn.parallel import DistributedDataParallel as DDP
import torch.distributed as dist
from torch.utils.data import DataLoader
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import os
import argparse
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument('--local_rank', default=0, type=int, help=('Used for multi-process training. Can either be manually set ' + "or automatically set by using 'python -m multiproc'."))
args = parser.parse_args()
dist.init_process_group(backend='nccl', init_method='env://', world_size=2, rank=args.local_rank)
torch.cuda.set_device(args.local_rank)
EPOCH = 2
BATCH_SIZE
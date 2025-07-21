'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.distributed.DistributedSampler\ntorch.utils.data.distributed.DistributedSampler(dataset, num_replicas=None, rank=None, shuffle=True, seed=0, drop_last=False)\n'
import torch
import torch.utils.data.distributed
dataset = torch.randn(100)
sampler = torch.utils.data.distributed.DistributedSampler(dataset, num_replicas=2, rank=0)
for i in sampler:
    print(i)
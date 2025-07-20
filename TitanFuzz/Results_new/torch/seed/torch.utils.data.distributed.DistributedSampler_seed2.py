dataset = torch.randn(100)
sampler = torch.utils.data.distributed.DistributedSampler(dataset, num_replicas=2, rank=0)
for i in sampler:
    print(i)
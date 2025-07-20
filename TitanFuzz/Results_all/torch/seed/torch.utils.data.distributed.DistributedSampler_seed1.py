data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_tensor = torch.tensor(data)
distributed_sampler = torch.utils.data.distributed.DistributedSampler(data_tensor, num_replicas=3, rank=0, shuffle=True, seed=0, drop_last=False)
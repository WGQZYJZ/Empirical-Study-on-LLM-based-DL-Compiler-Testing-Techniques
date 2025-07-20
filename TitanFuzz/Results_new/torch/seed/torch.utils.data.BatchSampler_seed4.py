data = torch.arange(0, 100)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.RandomSampler(data), batch_size=10, drop_last=False)
for i in batch_sampler:
    print(i)
sampler = torch.utils.data.RandomSampler(np.arange(10))
batch_sampler = torch.utils.data.BatchSampler(sampler, batch_size=3, drop_last=False)
for batch in batch_sampler:
    print(batch)
for batch in batch_sampler:
    print(batch)
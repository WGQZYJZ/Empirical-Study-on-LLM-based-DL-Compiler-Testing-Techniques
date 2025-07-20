data = torch.arange(1, 11)
batch_size = 3
sampler = torch.utils.data.BatchSampler(data, batch_size, drop_last=False)
for batch in sampler:
    print(batch)
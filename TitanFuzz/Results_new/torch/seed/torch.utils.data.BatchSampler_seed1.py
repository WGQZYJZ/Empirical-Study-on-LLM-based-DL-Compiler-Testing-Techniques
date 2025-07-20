data = list(range(10))
sampler = torch.utils.data.BatchSampler(data, batch_size=2, drop_last=True)
for batch in sampler:
    print(batch)
data = list(range(10))
sampler = torch.utils.data.BatchSampler(data, batch_size=2, drop_last=False)
data = torch.randint(low=0, high=100, size=(20,))
sampler = torch.utils.data.BatchSampler(torch.utils.data.RandomSampler(data), batch_size=5, drop_last=False)
for batch in sampler:
    print(f'batch: {batch}')
    print(f'data[batch]: {data[batch]}')
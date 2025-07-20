data = np.arange(100)
sampler = torch.utils.data.BatchSampler(data, 5, drop_last=True)
for i in sampler:
    print(i)
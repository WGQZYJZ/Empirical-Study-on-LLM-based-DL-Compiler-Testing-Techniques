data = np.random.randint(0, 100, size=100)
sampler = torch.utils.data.BatchSampler(data, batch_size=5, drop_last=False)
for i in sampler:
    print(i)
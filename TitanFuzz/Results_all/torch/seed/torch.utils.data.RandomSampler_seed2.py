data_source = list(range(10))
sampler = torch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)
data_source = np.random.randint(1, 100, (100,))
sampler = torch.utils.data.RandomSampler(data_source)
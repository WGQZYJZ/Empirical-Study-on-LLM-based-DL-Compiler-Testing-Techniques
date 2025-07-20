data_size = 100
data = np.random.rand(data_size, 3)
indices = np.random.choice(data_size, size=int((data_size * 0.8)), replace=False)
indices_test = np.array(list((set(range(data_size)) - set(indices))))
sampler = torch.utils.data.SubsetRandomSampler(indices)
sampler_test = torch.utils.data.SubsetRandomSampler(indices_test)
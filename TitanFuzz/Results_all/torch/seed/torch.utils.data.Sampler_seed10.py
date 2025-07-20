data_source = list(range(10))
sampler = torch.utils.data.Sampler(data_source)
data_source = list(range(10))
sampler = torch.utils.data.SequentialSampler(data_source)
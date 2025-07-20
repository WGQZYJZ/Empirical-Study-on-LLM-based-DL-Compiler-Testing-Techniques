data_source = [i for i in range(10)]
sampler = torch.utils.data.RandomSampler(data_source)
for i in range(10):
    print('sampler.__iter__()[{}]: '.format(i), sampler.__iter__().__next__())
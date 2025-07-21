'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)\n'
import torch
import torch.utils.data
data_source = [i for i in range(10)]
print('data_source: ', data_source)
sampler = torch.utils.data.RandomSampler(data_source)
for i in range(10):
    print('sampler.__iter__()[{}]: '.format(i), sampler.__iter__().__next__())
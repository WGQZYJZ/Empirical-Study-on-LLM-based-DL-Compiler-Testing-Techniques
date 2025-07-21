'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch.utils.data
data_size = 100
data = torch.rand(data_size)
batch_size = 10
batch_sampler = torch.utils.data.BatchSampler(torch.utils.data.sampler.SubsetRandomSampler(range(data_size)), batch_size=batch_size, drop_last=False)
print('batch_sampler:', batch_sampler)
print('len(batch_sampler):', len(batch_sampler))
for (i, batch_indices) in enumerate(batch_sampler):
    print('batch_indices:', batch_indices)
    print('data[batch_indices]:', data[batch_indices])
    print(('-' * 20))
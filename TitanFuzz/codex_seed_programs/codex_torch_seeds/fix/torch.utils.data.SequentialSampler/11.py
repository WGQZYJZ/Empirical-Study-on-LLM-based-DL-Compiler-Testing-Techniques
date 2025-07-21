'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
import torch.utils.data
data = torch.rand(10)
sampler = torch.utils.data.SequentialSampler(data)
for i in sampler:
    print('i = ', i)
'\nTask 4: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source)\n'
sampler = torch.utils.data.RandomSampler(data)
for i in sampler:
    print('i = ', i)
'\nTask 5: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices)\n'
indices = torch.LongTensor([0, 2, 4, 6, 8])
sampler = torch.utils.data.SubsetRandomSampler(indices)
for i in sampler:
    print('i = ', i)
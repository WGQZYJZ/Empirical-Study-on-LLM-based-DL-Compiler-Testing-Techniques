'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Sampler\ntorch.utils.data.Sampler(data_source)\n'
import torch
import torch.utils.data
input_data = torch.rand(5, 3)
sampler = torch.utils.data.Sampler(input_data)
print(sampler)
'\nTask 4: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
batch_sampler = torch.utils.data.BatchSampler(sampler, batch_size=2, drop_last=True)
print(batch_sampler)
'\nTask 5: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
sequential_sampler = torch.utils.data.SequentialSampler
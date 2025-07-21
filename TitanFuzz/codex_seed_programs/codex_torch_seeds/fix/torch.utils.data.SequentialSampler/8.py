'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
import torch.utils.data
input_data = torch.rand(5)
sampler = torch.utils.data.SequentialSampler(input_data)
for i in sampler:
    print(i)
print(sampler.__len__())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
input_data = torch.rand(5)
print(input_data)
sampler = torch.utils.data.SequentialSampler(input_data)
print(sampler)
for i in sampler:
    print(i)
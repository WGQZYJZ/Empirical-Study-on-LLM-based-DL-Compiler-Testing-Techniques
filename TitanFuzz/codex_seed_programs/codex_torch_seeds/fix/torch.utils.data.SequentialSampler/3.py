'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
input_data = torch.arange(0, 9)
sampler = torch.utils.data.SequentialSampler(input_data)
for i in sampler:
    print(i)
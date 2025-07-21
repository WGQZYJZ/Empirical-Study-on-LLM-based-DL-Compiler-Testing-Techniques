'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
import torch.utils.data
input_data = torch.randn(10, 3, 224, 224)
sampler = torch.utils.data.SequentialSampler(input_data)
print(sampler.__len__())
for i in range(10):
    index = sampler.__iter__().__next__()
    print(index)
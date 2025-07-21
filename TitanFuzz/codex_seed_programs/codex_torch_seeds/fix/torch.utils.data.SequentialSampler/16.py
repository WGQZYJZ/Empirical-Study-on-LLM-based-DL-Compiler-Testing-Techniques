'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
input_data = [i for i in range(10)]
sampler = torch.utils.data.SequentialSampler(input_data)
print('sampler: ', sampler)
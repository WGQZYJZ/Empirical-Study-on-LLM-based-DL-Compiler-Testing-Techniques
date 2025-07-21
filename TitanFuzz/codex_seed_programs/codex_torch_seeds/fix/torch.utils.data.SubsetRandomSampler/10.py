'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
import torch
input_data = torch.randint(low=0, high=100, size=(10,))
print(input_data)
sampler = torch.utils.data.SubsetRandomSampler(indices=input_data)
print(sampler)
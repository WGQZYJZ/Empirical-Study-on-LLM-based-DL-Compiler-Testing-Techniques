'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
import torch.utils.data as data
input_data = torch.arange(0, 10)
print(input_data)
sampler = torch.utils.data.Subset(input_data, [1, 3, 5, 7])
print(sampler)
for i in sampler:
    print(i)
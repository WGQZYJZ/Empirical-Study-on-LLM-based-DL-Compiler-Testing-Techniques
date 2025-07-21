'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
import torch
dataset = torch.utils.data.TensorDataset(torch.randn(100, 3), torch.randn(100))
sampler = torch.utils.data.SequentialSampler(dataset)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=4, sampler=sampler)
for (i, (inputs, labels)) in enumerate(dataloader):
    print(inputs, labels)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source)\n'
import torch
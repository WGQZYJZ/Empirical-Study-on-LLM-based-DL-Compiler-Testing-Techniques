'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ConcatDataset\ntorch.utils.data.ConcatDataset(datasets)\n'
import torch
import torch
dataset1 = torch.utils.data.TensorDataset(torch.rand(1000, 3), torch.rand(1000))
dataset2 = torch.utils.data.TensorDataset(torch.rand(1000, 3), torch.rand(1000))
dataset = torch.utils.data.ConcatDataset([dataset1, dataset2])
print(dataset[0])
print(dataset[1000])
dataset = torch.utils.data.Subset(dataset, range(10))
print(dataset[0])
print(dataset[9])
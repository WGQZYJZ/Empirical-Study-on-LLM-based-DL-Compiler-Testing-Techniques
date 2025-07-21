'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ConcatDataset\ntorch.utils.data.ConcatDataset(datasets)\n'
import torch
dataset1 = torch.randn(100, 2)
dataset2 = torch.randn(100, 2)
dataset = torch.utils.data.ConcatDataset([dataset1, dataset2])
print(dataset)
print(len(dataset))
print(dataset[0])
print(dataset[(- 1)])
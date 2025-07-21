'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ConcatDataset\ntorch.utils.data.ConcatDataset(datasets)\n'
import torch
from torch.utils.data import TensorDataset, DataLoader
import torch
x = torch.randn(100, 3)
y = torch.randint(low=0, high=2, size=(100, 1))
dataset1 = TensorDataset(x, y)
x = torch.randn(100, 3)
y = torch.randint(low=0, high=2, size=(100, 1))
dataset2 = TensorDataset(x, y)
dataset = torch.utils.data.ConcatDataset([dataset1, dataset2])
print(len(dataset))
print(dataset[0])
print(dataset[(- 1)])
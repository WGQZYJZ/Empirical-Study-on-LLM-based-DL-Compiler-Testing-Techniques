'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ConcatDataset\ntorch.utils.data.ConcatDataset(datasets)\n'
import torch
from torch.utils.data import ConcatDataset
import torch
dataset_1 = torch.randn(10, 2)
dataset_2 = torch.randn(10, 2)
dataset = ConcatDataset([dataset_1, dataset_2])
for i in range(len(dataset)):
    print(dataset[i])
print('The dataset size is: ', len(dataset))
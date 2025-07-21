'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ConcatDataset\ntorch.utils.data.ConcatDataset(datasets)\n'
import torch
from torch.utils.data import TensorDataset, ConcatDataset
import torch
input_data1 = torch.randn(2, 5)
input_data2 = torch.randn(2, 5)
input_data3 = torch.randn(2, 5)
dataset1 = TensorDataset(input_data1)
dataset2 = TensorDataset(input_data2)
dataset3 = TensorDataset(input_data3)
datasets = [dataset1, dataset2, dataset3]
concat_dataset = ConcatDataset(datasets)
print(concat_dataset)
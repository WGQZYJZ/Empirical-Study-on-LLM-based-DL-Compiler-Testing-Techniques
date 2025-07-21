'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ConcatDataset\ntorch.utils.data.ConcatDataset(datasets)\n'
import torch
import torch.utils.data
import torch
input_data1 = torch.randn(5, 3)
input_data2 = torch.randn(5, 3)
dataset = torch.utils.data.ConcatDataset([input_data1, input_data2])
print(dataset)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(tensors)\n'
import torch
import torch.utils.data
import torch
input_data1 = torch.randn(5, 3)
input_data2 = torch.randn(5, 3)
dataset = torch.utils.data.TensorDataset(input_data1, input_data2)
print(dataset)
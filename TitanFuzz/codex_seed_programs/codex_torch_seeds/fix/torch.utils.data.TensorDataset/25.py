'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
from torch.utils.data import TensorDataset
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = torch.tensor([0, 1, 2])
dataset = TensorDataset(x, y)
print(dataset[0])
print(dataset[0][0])
print(dataset[0][1])
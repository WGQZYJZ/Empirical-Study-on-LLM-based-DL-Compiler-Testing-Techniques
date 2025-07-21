'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([[1], [2], [3]])
dataset = torch.utils.data.TensorDataset(torch.from_numpy(x), torch.from_numpy(y))
print(dataset)
print(dataset.__len__())
print(dataset[0])
print(dataset[1])
print(dataset[2])
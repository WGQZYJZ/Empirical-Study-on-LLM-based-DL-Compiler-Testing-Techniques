'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import torch
x = torch.tensor([[1, 2], [3, 4], [5, 6]])
y = torch.tensor([[1], [2], [3]])
torch.utils.data.TensorDataset(x, y)
dataset = torch.utils.data.TensorDataset(x, y)
dataset[0]
dataset[1]
dataset[2]
dataset[0][0]
dataset[0][1]
dataset[1][0]
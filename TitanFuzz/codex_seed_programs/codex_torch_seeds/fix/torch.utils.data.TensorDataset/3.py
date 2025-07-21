'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
from torch.utils.data import TensorDataset
import torch
from torch.utils.data import TensorDataset
x = torch.tensor([[1, 2], [3, 4], [5, 6]])
y = torch.tensor([[10], [20], [30]])
ds = TensorDataset(x, y)
print(ds)
print(ds[0])
print(ds[0][0])
print(ds[0][1])
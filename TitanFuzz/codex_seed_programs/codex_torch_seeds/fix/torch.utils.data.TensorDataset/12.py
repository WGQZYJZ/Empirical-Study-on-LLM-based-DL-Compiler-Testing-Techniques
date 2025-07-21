'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import torch
x_data = torch.tensor([[1.0], [2.0], [3.0]])
y_data = torch.tensor([[2.0], [4.0], [6.0]])
ds = TensorDataset(x_data, y_data)
loader = DataLoader(ds, batch_size=2, shuffle=True)
for epoch in range(3):
    for (x_batch, y_batch) in loader:
        print(epoch, x_batch.numpy(), y_batch.numpy())
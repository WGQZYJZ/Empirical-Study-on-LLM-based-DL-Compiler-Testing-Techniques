'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import torch.utils.data
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
x = torch.randn(5, 3)
y = torch.randn(5, 2)
tensor_dataset = TensorDataset(x, y)
data_loader = DataLoader(tensor_dataset, batch_size=2, shuffle=True)
for (x_batch, y_batch) in data_loader:
    print(x_batch)
    print(y_batch)
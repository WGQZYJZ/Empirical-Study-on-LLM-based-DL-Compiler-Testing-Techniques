'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
x = torch.randn(3, 3)
y = torch.randn(3, 2)
print(x)
print(y)
data = torch.utils.data.TensorDataset(x, y)
print(data)
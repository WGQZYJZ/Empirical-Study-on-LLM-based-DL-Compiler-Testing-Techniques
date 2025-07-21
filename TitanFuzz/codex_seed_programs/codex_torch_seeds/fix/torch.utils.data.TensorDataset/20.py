'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
x = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
y = torch.tensor([[1], [2], [3], [4]])
tensor_dataset = torch.utils.data.TensorDataset(x, y)
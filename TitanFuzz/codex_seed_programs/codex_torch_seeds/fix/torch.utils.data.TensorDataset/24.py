'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import torch.utils.data
import torch
import torch.utils.data
x = torch.Tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
y = torch.Tensor([[1], [2], [3], [4]])
dataset = torch.utils.data.TensorDataset(x, y)
print(dataset)
for i in range(len(dataset)):
    print(dataset[i])
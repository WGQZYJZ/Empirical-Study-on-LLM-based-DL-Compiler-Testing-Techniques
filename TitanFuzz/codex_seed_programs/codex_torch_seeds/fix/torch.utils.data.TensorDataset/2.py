'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = torch.tensor([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
dataset = torch.utils.data.TensorDataset(x, y)
print(dataset)
print(dataset.tensors)
print(dataset[0])
print(dataset[0][0])
print(dataset[0][1])
print(dataset[1])
print(dataset[1][0])
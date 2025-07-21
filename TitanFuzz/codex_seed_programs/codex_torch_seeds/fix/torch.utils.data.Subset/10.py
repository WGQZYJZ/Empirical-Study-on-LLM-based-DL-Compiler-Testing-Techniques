'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
import torch.utils.data as data
import torch
import torch.utils.data as data
input_data = torch.randn(100, 3)
labels = torch.randint(0, 2, (100,))
dataset = data.TensorDataset(input_data, labels)
idx = torch.randperm(100)
train_dataset = data.Subset(dataset, idx[:80])
test_dataset = data.Subset(dataset, idx[80:])
print('train_dataset:', train_dataset)
print('test_dataset:', test_dataset)
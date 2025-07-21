'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torch.utils.data import Subset
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torch.utils.data import Subset
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
label_data = torch.tensor([1, 2, 3, 4])
dataset = TensorDataset(input_data, label_data)
train_dataset = Subset(dataset, [0, 1])
print('train_dataset: ', train_dataset)
test_dataset = Subset(dataset, [2, 3])